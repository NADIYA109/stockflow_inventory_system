## Issue 1: No input validation

Impact:

If any required field (like name, sku, price, etc.) is missing from the request, the app will crash with a KeyError.

Fix:

Add a check to ensure all required fields are present before using them.

## Issue 2: No check for unique SKU

Impact:

Duplicate SKUs can be created, which may cause problems for inventory tracking and product identification.

Fix:

Check in the database if a product with the same SKU already exists before creating a new one.

## Issue 3: Saving warehouse_id in the Product model

Impact:

A product can exist in multiple warehouses, so saving warehouse_id in the product table is logically wrong.
Fix:

Remove warehouse_id from the Product model and instead manage warehouse-product relationships through the Inventory table.

## Issue 4: Price is not handled as a Decimal

Impact:

Using float values for price can lead to rounding and calculation issues during billing.

Fix:

Convert the price to Decimal type before saving.

## Issue 5: No error handling (try-except missing)

Impact:

If any step fails (like database error), the app will crash, and the user will not get any helpful error message.

Fix:

Wrap the logic in a try-except block and return meaningful error messages.

## Issue 6: No db.session.rollback() on error

Impact:

If inventory saving fails after product is saved, it will leave incomplete data. Also, for errors like duplicate SKU, rollback is needed.

Fix:

Use db.session.rollback() in both except blocks(one for general exceptions and one for database integrity errors) to cancel changes if something goes wrong.
