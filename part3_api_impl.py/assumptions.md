While implementing this API, some database details and business logic were not fully given. So, I made the following assumptions to complete the task.

## Assumptions:

1. 'min_stock_limit' column is present in the 'products' table to store low stock threshold.

2. Recent sales activity is identified by checking 'inventory_history' table where 'stock_change < 0' in the last 30 days.

3. Products can be linked to suppliers using a 'product_suppliers' table (many-to-many).

4. One product can have multiple suppliers, but we are just showing the first one in the alert.

5. 'inventory' table has 'product_id', 'warehouse_id', and 'quantity' columns.

6. 'Warehouse' model has a 'company_id' column that connects it to the 'companies' table.

7. If sales are 0, we assume average daily sales = 1 to avoid division by 0.

8. We assume 'date' column in 'inventory_history' table is used to filter recent changes.
