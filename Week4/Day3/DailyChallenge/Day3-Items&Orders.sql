-- Daily challenge : Items & Orders
-- Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.
--
-- There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.
--
-- Create a function that returns the total price for a given order.

CREATE TABLE product_orders(
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

CREATE TABLE items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_name VARCHAR(50),
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES product_orders(order_id)
);

CREATE OR REPLACE FUNCTION get_order_total_price(order_id INT)
  RETURNS DECIMAL(10,2) AS $$
DECLARE
  total_price DECIMAL(10,2);
BEGIN
  SELECT SUM(price) INTO total_price
  FROM items
  WHERE items.order_id = get_order_total_price.order_id;

  RETURN total_price;
END;
$$ LANGUAGE plpgsql;

-- Bonus :
--
--     Create a table called users.
--     There should be a one to many relationship between the users table and the product_orders table.
--     Create a function that returns the total price for a given order of a given user.


CREATE TABLE users (
  user_id INT PRIMARY KEY,
  username VARCHAR(50)
);

ALTER TABLE product_orders
RENAME COLUMN customer_id TO user_id;

ALTER TABLE product_orders
ADD FOREIGN KEY (user_id) REFERENCES users(user_id);


CREATE OR REPLACE FUNCTION get_order_total_price(user_id INT, order_id INT)
RETURNS DECIMAL(10, 2) AS $$
DECLARE
    total_price DECIMAL(10, 2);
BEGIN
    SELECT SUM(items.price) INTO total_price
    FROM items
    INNER JOIN product_orders ON items.order_id = product_orders.order_id
    WHERE product_orders.user_id = get_order_total_price.user_id
      AND product_orders.order_id = get_order_total_price.order_id;

    RETURN total_price;
END;
$$ LANGUAGE plpgsql;