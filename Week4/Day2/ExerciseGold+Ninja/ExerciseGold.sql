-- Exercise 1: DVD Rental
-- Instructions
--     You were hired to babysit your cousin and you want to find a few movies that he can watch with you.

-- 1. Find out how many films there are for each rating.
SELECT rating, count(*) as film_count
FROM film
GROUP BY rating;

-- 2. Get a list of all the movies that have a rating of G or PG-13.
SELECT *
FROM film
WHERE rating = 'G'
   or rating = 'PG-13';

--      Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
SELECT *
FROM film
WHERE rating in ('G', 'PG-13')
  AND length < 120
  AND rental_rate < 3.00
ORDER BY title;

-- 3. Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
UPDATE customer
SET first_name='Ally',
    last_name='Ke',
    email='ally.ke@example.com'
WHERE customer_id = 524;

-- 4. Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
UPDATE address
SET address='1234 Elm Street'
WHERE address_id = (SELECT address_id from customer WHERE first_name = 'Ally');


---------------------------------------------------------------------------------
-- Exercise 2: students table

-- # Update
-- 1. Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
UPDATE students
SET birth_date='1998-02-11'
WHERE last_name = 'Benichou';

-- 2. Change the last_name of David from ‘Grez’ to ‘Guez’.
UPDATE students
SET last_name='Guez'
WHERE first_name = 'David';

-- # Delete
-- 1. Delete the student named ‘Lea Benichou’ from the table.
DELETE
FROM students
WHERE last_name = 'Benichou'
  AND first_name = 'Lea';

-- # Count
-- 1. Count how many students are in the table.
SELECT count(*)
FROM students;

-- 2. Count how many students were born after 1/01/2000.
SELECT count(*)
from students
WHERE birth_date > '2000-01-01';


-- # Insert / Alter
-- 1. Add a column to the student table called math_grade.
ALTER TABLE students
    ADD math_grade SMALLINT;

-- 2. Add 80 to the student which id is 1.
UPDATE students
SET math_grade=80
WHERE id = 1;

-- 3. Add 90 to the students which have ids of 2 or 4.
UPDATE students
SET math_grade=90
WHERE id in (2, 4);

-- 4. Add 40 to the student which id is 6.
UPDATE students
SET math_grade=40
WHERE id = 6;


-- 5. Count how many students have a grade bigger than 83
SELECT count(*)
FROM students
WHERE math_grade > 83;

-- 6. Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students (first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', '1980-10-03', 70);

-- 7. Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam.
SELECT count(*)
FROM students
where first_name = 'Omer';

--      Bonus: Count how many grades each student has.
SELECT first_name || ' ' || last_name as full_name, count(*) as total_grade
From students
GROUP BY full_name;


-- # SUM
-- Find the sum of all the students grades.
SELECT sum(math_grade) as all_students_grade
FROM students;


------------------------------------------------------------------------------------------
-- Exercise 3 : Items and customers

-- Part I
-- 1. Create a table named purchases. It should have 3 columns :
--     id : the primary key of the table
--     customer_id : this column references the table customers
--     item_id : this column references the table items
--     quantity_purchased : this column is the quantity of items purchased by a certain customer

CREATE TABLE purchases
(
    id                 serial PRIMARY KEY,
    customer_id        smallint REFERENCES customers (customer_id),
    item_id            smallint REFERENCES items (item_id),
    quantity_purchased smallint
);

-- 2. Insert purchases for the customers, use subqueries:
--     Scott Scott bought one fan
--     Melanie Johnson bought ten large desks
--     Greg Jones bougth two small desks

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES ((SELECT customer_id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
        (SELECT item_id from items where item_name = 'Fan'), 1),
       ((SELECT customer_id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
        (SELECT item_id from items where item_name = 'Large Desk'), 10),
       ((SELECT customer_id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
        (SELECT item_id from items where item_name = 'Small Desk'), 2);


-- Part II
--    # Use SQL to get the following from the database:
-- 1. All purchases. Is this information useful to us?
SELECT *
from purchases;

-- 2. All purchases, joining with the customers table.
SELECT *
from purchases p
         JOIN customers c on c.customer_id = p.customer_id;

-- 3. Purchases of the customer with the ID equal to 5.
SELECT *
from purchases
WHERE customer_id = 5;

-- 4. Purchases for a large desk AND a small desk
SELECT *
FROM purchases
WHERE item_id IN (SELECT item_id
                  FROM items
                  WHERE item_name IN ('Large Desk', 'Small Desk'));

-- # Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name ; Customer last name; Item name
SELECT c.first_name, c.last_name, i.item_name
FROM customers c
         JOIN purchases p ON c.customer_id = p.customer_id
         JOIN items i ON p.item_id = i.item_id;

-- Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
--      the insertion will likely fail because the foreign key constraint requires the "item_id" to have a valid reference to an existing item ID in the "items" table.
