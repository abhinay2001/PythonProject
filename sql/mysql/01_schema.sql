CREATE DATABASE IF NOT EXISTS retail_db;
USE retail_db;

CREATE TABLE IF NOT EXISTS departments (
  department_id INT PRIMARY KEY,
  department_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
  category_id INT PRIMARY KEY,
  category_department_id INT,
  category_name VARCHAR(255),
  INDEX (category_department_id)
);

CREATE TABLE IF NOT EXISTS products (
  product_id INT PRIMARY KEY,
  product_category_id INT,
  product_name VARCHAR(255),
  product_description TEXT,
  product_price DECIMAL(10,2),
  product_image VARCHAR(255),
  INDEX (product_category_id)
);

CREATE TABLE IF NOT EXISTS customers (
  customer_id INT PRIMARY KEY,
  customer_fname VARCHAR(255),
  customer_lname VARCHAR(255),
  customer_email VARCHAR(255),
  customer_password VARCHAR(255),
  customer_street VARCHAR(255),
  customer_city VARCHAR(255),
  customer_state VARCHAR(255),
  customer_zipcode VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS orders (
  order_id INT PRIMARY KEY,
  order_date DATETIME,
  order_customer_id INT,
  order_status VARCHAR(50),
  INDEX (order_customer_id)
);

CREATE TABLE IF NOT EXISTS order_items (
  order_item_id INT PRIMARY KEY,
  order_item_order_id INT,
  order_item_product_id INT,
  order_item_quantity INT,
  order_item_subtotal DECIMAL(10,2),
  order_item_product_price DECIMAL(10,2),
  INDEX (order_item_order_id),
  INDEX (order_item_product_id)
);
