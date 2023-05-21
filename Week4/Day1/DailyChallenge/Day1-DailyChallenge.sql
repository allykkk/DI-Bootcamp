-- Daily challenge : Actors
-- Instructions
--
-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?

SELECT count(*) as actor_count from actors;

INSERT INTO actors (first_name, last_name, date_birth)
VALUES ('John', '', '1990-05-15');
-- ERROR: null value in column "first_name" violates not-null constraint