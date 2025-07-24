# StockFlow – Inventory Management System (B2B SaaS)
This project is part of a backend internship task. It's an inventory management system called StockFlow, designed for small businesses to track products across warehouses and manage supplier relationships.

# Project Parts

# Part 1 Code Review & Debugging

.Reviewed and fixed a product creation API.
.Issues included missing validations, no error handling, and wrong business logic.
.Added proper checks for SKU uniqueness, required fields, and warehouse-product mapping.
.Error handling added using try-except and rollback.

# Part 2 – Database Design

.Designed a simple database schema to support all features.
.Includes tables for companies, warehouses, products, inventory, suppliers, etc.
.Supports bundle products, multiple suppliers, and inventory history.

# Part 3 – Low Stock Alert API

.Created a Flask API to get low-stock alerts for a company.
.Follows business rules like:
  .Only show if there was recent sales
  .Check product’s custom stock limit
  .Include supplier info
.Handled edge cases like no sales, missing supplier, zero division, etc.


 