-- Exercise 1 : Bonus Public Database (Continuation of XP)

-- 1. Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT first_name, last_name
FROM customers
ORDER BY last_name DESC
LIMIT 2;

-- 2. Use SQL to delete all purchases made by Scott.
DELETE FROM purchases
Where customer_id = (SELECT customer_id from customers where first_name='Scott');


-- 3. Does Scott still exist in the customers table, even though he has been deleted? Try and find him.
SELECT * from customers
WHERE first_name='Scott';

-- 4. Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will appear, although instead of the customer’s first and last name, you should only see empty/blank. (Which kind of join should you use?).
SELECT * from purchases
RIGHT JOIN customers ON purchases.customer_id = customers.customer_id;

-- 5. Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will NOT appear.
SELECT * from purchases
LEFT JOIN customers ON purchases.customer_id = customers.customer_id;



