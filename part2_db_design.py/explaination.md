# Database Design Explanation

.companies – stores company information
.warehouses – each warehouse belongs to a company
.products – has name, SKU, price, min_stock_limit, and type (single/bundle)
.inventory – shows how much quantity is available in each warehouse
.inventory_history – logs inventory changes with reason and date
.suppliers – stores supplier name and contact email
.product_suppliers – connects products and suppliers (many-to-many)
.product_bundles – allows one product to be made from other products (for combos)


# Design Decisions

.Used separate tables to keep data clean and organized
.Foreign keys used to link related tables properly.
.Made SKU unique, because each product should have a unique code
.Used a many-to-many table for products and suppliers
.Added an inventory history table to track all stock changes
.Set default values like min_stock_limit = 10 and type = single to avoid nulls
.Used simple column names to make it easy for anyone to understand later

# Missing Questions

.Can product price vary in different warehouses or suppliers?
.Do we need to store when a product is sold and to whom?
.Can one supplier supply to multiple companies?
.When a bundle is sold, should all items inside reduce from stock?
.Do we allow negative stock (below 0) or block it?
.Do we need to store who changed the inventory (admin/user ID)?




