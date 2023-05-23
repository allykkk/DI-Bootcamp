-- 🌟 Exercise 1: DVD Rental

-- 1. Get a list of all film languages.
SELECT name
FROM language;

-- 2. Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
--    (1) Get all films, even if they don’t have languages.
SELECT f.title, f.description, lg.name
from film f
         LEFT JOIN language lg on f.language_id = lg.language_id;

--    (2) Get all languages, even if there are no films in those languages.
SELECT f.title, f.description, lg.name
from film f
         RIGHT JOIN language lg on f.language_id = lg.language_id;


-- 3. Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE table new_film
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name)
VALUES ('Detachment'),
       ('Donnie Darko'),
       ('12 Angry Men');

-- 4. Create a new table called customer_review, which will contain film reviews that customers will make.
--    Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
--    It should have the following columns:
--     review_id – a primary key, non null, auto-increment.
--     film_id – references the new_film table. The film that is being reviewed.
--     language_id – references the language table. What language the review is in.
--     title – the title of the review.
--     score – the rating of the review (1-10).
--     review_text – the text of the review. No limit on the length.
--     last_update – when the review was last updated.

CREATE table customer_review
(
    review_id   SERIAL PRIMARY KEY,
    film_id     INT REFERENCES new_film (id) on DELETE CASCADE,
    language_id INT REFERENCES language (language_id),
    title       VARCHAR(255),
    score       INT,
    review_text TEXT,
    last_update TIMESTAMP
);

-- 5. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES (1, 1, 'Great movie!', 9, 'I really enjoyed watching this movie. The acting and storyline were fantastic.',
        NOW()),
       (2, 2, 'Disappointing', 5, 'The movie had potential, but it fell short in execution. Not worth the hype.',
        NOW());

-- 6. Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE
FROM new_film
WHERE id = 2;
--          review is deleted as well

-----------------------------------------------------------------------
-- 🌟 Exercise 2 : DVD Rental
-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id=2
WHERE film_id between 200 and 250;

-- 2. Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
--     address id, need to ensure the foreign key already exist in the referenced table.

-- 3. We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review;
--     It was easy, because other tables has no dependency on this one.

-- 4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT count(*) AS outstanding_rentals
FROM rental
WHERE return_date is NULL;

-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT f.film_id, f.title, r.return_date, f.rental_rate
FROM film f
         JOIN inventory i ON f.film_id = i.film_id
         JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;

-- 6. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
--      (1) The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT f.film_id, f.title, f.fulltext
from film f
         join film_actor fa on f.film_id = fa.film_id
         join actor a on fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope'
  and a.last_name = 'Monroe'
  and f.fulltext @@ to_tsquery('sumo | wrestler');

--      (2) The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT f.film_id, f.title, c.name as category, f.length, f.rating
from film f
         join film_category fc on f.film_id = fc.film_id
         join category c on fc.category_id = c.category_id
where c.name = 'Documentary'
  and f.length < 60
  and f.rating = 'R';

--      (3) The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT f.film_id, f.title, c.first_name || ' ' || c.last_name AS customer_name, f.rental_rate, r.rental_date
from film f
         join inventory i on f.film_id = i.film_id
         join rental r on i.inventory_id = r.inventory_id
         join customer c on r.customer_id = c.customer_id
WHERE (c.first_name || ' ' || c.last_name) = 'Matthew Mahan'
  and f.rental_rate > 4.00
  and r.rental_date between '2005-07-28' and '2005-08-01';

--      (4) The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT f.film_id, f.title, c.first_name || ' ' || c.last_name AS customer_name, f.description, f.replacement_cost
from film f
         join inventory i on f.film_id = i.film_id
         join rental r on i.inventory_id = r.inventory_id
         join customer c on r.customer_id = c.customer_id
WHERE (c.first_name || ' ' || c.last_name) = 'Matthew Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC LIMIT 1;