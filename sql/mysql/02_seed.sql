USE retail_db;

-- Departments
INSERT INTO departments (department_id, department_name) VALUES
(1,'Fitness'),
(2,'Apparel'),
(3,'Footwear')
ON DUPLICATE KEY UPDATE department_name=VALUES(department_name);

-- Categories
INSERT INTO categories (category_id, category_department_id, category_name) VALUES
(1,1,'Cardio'),
(2,1,'Strength'),
(3,2,'Men'),
(4,2,'Women'),
(5,3,'Running')
ON DUPLICATE KEY UPDATE
category_department_id=VALUES(category_department_id),
category_name=VALUES(category_name);

-- Products
INSERT INTO products (product_id, product_category_id, product_name, product_description, product_price, product_image) VALUES
(1,1,'Treadmill Pro','High-end treadmill',1299.99,'treadmill.png'),
(2,2,'Dumbbell Set','Adjustable dumbbells',249.99,'dumbbells.png'),
(3,3,'Men T-Shirt','Cotton tee',19.99,'mens_tee.png'),
(4,4,'Women Leggings','Stretch leggings',39.99,'leggings.png'),
(5,5,'Running Shoes','Lightweight shoes',89.99,'shoes.png')
ON DUPLICATE KEY UPDATE
product_category_id=VALUES(product_category_id),
product_name=VALUES(product_name),
product_description=VALUES(product_description),
product_price=VALUES(product_price),
product_image=VALUES(product_image);

-- Customers
INSERT INTO customers (customer_id, customer_fname, customer_lname, customer_email, customer_password,
customer_street, customer_city, customer_state, customer_zipcode) VALUES
(1,'Abhi','Dhire','abhi@example.com','x','1 Main St','San Jose','CA','95112'),
(2,'Sam','Lee','sam@example.com','x','2 Oak St','San Mateo','CA','94401')
ON DUPLICATE KEY UPDATE
customer_fname=VALUES(customer_fname),
customer_lname=VALUES(customer_lname),
customer_email=VALUES(customer_email);

-- Orders
INSERT INTO orders (order_id, order_date, order_customer_id, order_status) VALUES
(1,'2025-12-20 10:00:00',1,'COMPLETE'),
(2,'2025-12-21 11:30:00',2,'PENDING')
ON DUPLICATE KEY UPDATE
order_date=VALUES(order_date),
order_customer_id=VALUES(order_customer_id),
order_status=VALUES(order_status);

-- Order Items
INSERT INTO order_items (order_item_id, order_item_order_id, order_item_product_id, order_item_quantity,
order_item_subtotal, order_item_product_price) VALUES
(1,1,1,1,1299.99,1299.99),
(2,1,2,1,249.99,249.99),
(3,2,3,2,39.98,19.99)
ON DUPLICATE KEY UPDATE
order_item_order_id=VALUES(order_item_order_id),
order_item_product_id=VALUES(order_item_product_id),
order_item_quantity=VALUES(order_item_quantity),
order_item_subtotal=VALUES(order_item_subtotal),
order_item_product_price=VALUES(order_item_product_price);
