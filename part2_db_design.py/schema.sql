/*Companies table*/
CREATE TABLE companies (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

 /*Warehouses table*/ 
CREATE TABLE warehouses (
  id INT PRIMARY KEY,
  company_id INT,
  name VARCHAR(100),
  location VARCHAR(100),
  FOREIGN KEY (company_id) REFERENCES companies(id)
);

/*Products table*/
CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  sku VARCHAR(50) UNIQUE,
  price DECIMAL(8, 2),
  min_stock_limit INT DEFAULT 10 
  type VARCHAR(50) DEFAULT 'single'
);

/*Inventory table (stores product quantity per warehouse)*/
CREATE TABLE inventory (
  id INT PRIMARY KEY,
  product_id INT,
  warehouse_id INT,
  quantity INT,
  FOREIGN KEY (product_id) REFERENCES products(id),
  FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
);

/*Inventory history table (to track stock changes)*/
CREATE TABLE inventory_history (
  id INT PRIMARY KEY,
  inventory_id INT,
  stock_change INT,          
  reason VARCHAR(100), 
  date TIMESTAMP,
  FOREIGN KEY (inventory_id) REFERENCES inventory(id)
);

/*Suppliers table*/
CREATE TABLE suppliers (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

/*Product mapping table*/
CREATE TABLE product_suppliers (
  id INT PRIMARY KEY,
  product_id INT,
  supplier_id INT,
  FOREIGN KEY (product_id) REFERENCES products(id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

/*Bundled products table (for kits or combos)*/
CREATE TABLE product_bundles (
  id INT PRIMARY KEY,
  bundle_id INT,
  item_id INT,
  quantity INT,
  FOREIGN KEY (bundle_id) REFERENCES products(id),
  FOREIGN KEY (item_id) REFERENCES products(id)
);
