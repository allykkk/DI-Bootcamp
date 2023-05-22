-- 🌟 Exercise 1 : Items and customers
-- Instructions
--
-- We will work on the public database that we created yesterday.
-- Use SQL to get the following from the database:

-- All items, ordered by price (lowest to highest).
SELECT * from items ORDER BY price ;

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
SELECT * from items WHERE price>=80 ORDER BY price DESC ;

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
SELECT first_name, last_name from customers ORDER BY first_name LIMIT 3;

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT last_name from customers ORDER BY last_name DESC;


-------------------------------------------------------------------------
-- 🌟 Exercise 2 : Dvdrental database

-- We will use the newly installed dvdrental database.

-- 1. In the dvdrental database write a query to select all the columns from the “customer” table.
SELECT * from customer;

-- 2. Write a query to display the names (first_name, last_name) using an alias named “full_name”.
SELECT first_name || ' ' || last_name AS full_name from customer;

-- 3. Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
SELECT DISTINCT create_date from customer;

-- 4. Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
SELECT * from customer ORDER BY first_name DESC;

-- 5. Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT film_id,title,description,release_year,rental_rate from film ORDER BY rental_rate;

-- 6. Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
SELECT address,phone from address WHERE district='Texas';

-- 7. Write a query to retrieve all movie details where the movie id is either 15 or 150.
SELECT * from film WHERE film_id=15 or film_id=150;

-- 8. Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
SELECT film_id, title, description, length, rental_rate from film WHERE title='Kiss Glory'

-- 9. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
SELECT film_id, title, description, length, rental_rate from film WHERE title LIKE 'Ki%';

-- 10. Write a query which will find the 10 cheapest movies.
SELECT * from film ORDER BY rental_rate limit 10;

-- 11. Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
SELECT * from film ORDER BY rental_rate OFFSET 10 limit 10;

-- 12. Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id;

-- 13. You need to check your inventory. Write a query to get all the movies which are not in inventory.
SELECT film.film_id, film.title
FROM film
LEFT JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.inventory_id IS NULL;

-- 14. Write a query to find which city is in which country.
SELECT city.city, country.country
FROM city
JOIN country on city.country_id = country.country_id;

-- 15. Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name, p.amount, p.payment_date, p.staff_id
FROM customer AS c
JOIN payment AS p ON c.customer_id = p.customer_id
ORDER BY p.staff_id;


