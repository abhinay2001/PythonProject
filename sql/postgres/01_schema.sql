CREATE TABLE IF NOT EXISTS departments (
  department_id INT PRIMARY KEY,
  department_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
  category_id INT PRIMARY KEY,
  category_department_id INT,
  category_name TEXT
);

CREATE TABLE IF NOT EXISTS products (
  product_id INT PRIMARY KEY,
  product_category_id INT,
  product_name TEXT,
  product_description TEXT,
  product_price NUMERIC(10,2),
  product_image TEXT
);

CREATE TABLE IF NOT EXISTS customers (
  customer_id INT PRIMARY KEY,
  customer_fname TEXT,
  customer_lname TEXT,
  customer_email TEXT,
  customer_password TEXT,
  customer_street TEXT,
  customer_city TEXT,
  customer_state TEXT,
  customer_zipcode TEXT
);

CREATE TABLE IF NOT EXISTS orders (
  order_id INT PRIMARY KEY,
  order_date TIMESTAMP,
  order_customer_id INT,
  order_status TEXT
);

CREATE TABLE IF NOT EXISTS order_items (
  order_item_id INT PRIMARY KEY,
  order_item_order_id INT,
  order_item_product_id INT,
  order_item_quantity INT,
  order_item_subtotal NUMERIC(10,2),
  order_item_product_price NUMERIC(10,2)
);
