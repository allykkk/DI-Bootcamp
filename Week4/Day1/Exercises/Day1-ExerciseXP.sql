
-- Create a database called public.
CREATE DATABASE public;

-- Add two tables: items & customers
CREATE TABLE items
(
    item_id   serial primary key,
    item_name varchar(100),
    price     numeric(10, 2)
);

CREATE TABLE customers
(
    customer_id serial primary key,
    first_name  varchar(100),
    last_name   varchar(100)
);


-- 1. Add the following items to the items table:
INSERT INTO items(item_name, price)
VALUES ('Small Desk', 100),
       ('Large Desk', 300),
       ('Fan', 80);


-- 2. Add 5 new customers to the customers table:
INSERT INTO customers(first_name, last_name)
VALUES ('Greg', 'Jones'),
       ('Sandra', 'Jones'),
       ('Scott', 'Scott'),
       ('Trevor ', 'Green'),
       ('Melanie ', 'Johnson');


-- 3. Use SQL to fetch the following data from the database:

-- (1) All the items.
select * from items
-- (2) All the items with a price above 80 (80 not included).
select * from items where price > 80;
-- (3) All the items with a price below 300. (300 included)
select * from items where price <= 300;
-- (4) All customers whose last name is ‘Smith’ (What will be your outcome?).
select * from customers where last_name = 'Smith';
-- (5) All customers whose last name is ‘Jones’.
select * from customers where last_name = 'Jones';
-- (6) All customers whose firstname is not ‘Scott’.
select * from customers where first_name != 'Scott';


