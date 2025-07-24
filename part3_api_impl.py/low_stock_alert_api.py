from flask import Flask, jsonify
from datetime import datetime, timedelta
from models import db, Warehouse, Product, Inventory, InventoryHistory, ProductSupplier, Supplier

app = Flask(__name__)

@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    alerts = []

    # Get all warehouses of this company
    warehouses = Warehouse.query.filter_by(company_id=company_id).all()

    for warehouse in warehouses:
        # Get all products in this warehouse
        inventories = Inventory.query.filter_by(warehouse_id=warehouse.id).all()

        for inventory in inventories:
            product = Product.query.get(inventory.product_id)

            # Get product's threshold
            threshold = product.min_stock_limit

            # Check if there was any sale (stock decrease) in last 30 days
            thirty_days_ago = datetime.now() - timedelta(days=30)
            recent_sales = InventoryHistory.query.filter(
                InventoryHistory.inventory_id == inventory.id,
                InventoryHistory.stock_change < 0,
                InventoryHistory.date >= thirty_days_ago
            ).all()

            if not recent_sales:
                continue  # skip if no recent sales

            # Check if current stock is below threshold
            if inventory.quantity < threshold:
                # Calculate average daily sale
                total_sales = 0
                for sale in recent_sales:
                    total_sales += abs(sale.stock_change)

                if total_sales > 0:
                    avg_daily_sales = total_sales / 30
                else:
                    avg_daily_sales = 1  # to avoid divide by 0

                # Estimate days left before stock ends
                days_until_stockout = int(inventory.quantity / avg_daily_sales)

                # Get supplier info (just the first one)
                supplier_info = ProductSupplier.query.filter_by(product_id=product.id).first()
                supplier = Supplier.query.get(supplier_info.supplier_id) if supplier_info else None
                
                # Add this product to the alerts list
                alert = {
                    "product_id": product.id,
                    "product_name": product.name,
                    "sku": product.sku,
                    "warehouse_id": warehouse.id,
                    "warehouse_name": warehouse.name,
                    "current_stock": inventory.quantity,
                    "threshold": threshold,
                    "days_until_stockout": days_until_stockout,
                    "supplier": {
                        "id": supplier.id,
                        "name": supplier.name,
                        "contact_email": supplier.email
                    } if supplier else None
                }

                alerts.append(alert)
    
    # Return all alerts in JSON format
    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    }), 200
