-- 🌟 Exercise 1 : Bootcamp

-- 1. CREATE
-- (1) Create a database called bootcamp.
-- (2) Create a table called students.
-- (3) Add the following columns: id; last_name; first_name; birth_date
--     The id must be auto_incremented.
--     Make sure to choose the correct data type for each column.

CREATE DATABASE bootcamp;
CREATE TABLE students
(
    id         serial primary key,
    last_name  varchar(100),
    first_name varchar(100),
    birth_date date
);

-- 2. INSERT
-- (1) Insert the data seen above to the students table. Find the most efficient way to insert the data.
-- (2) Insert your last_name, first_name and birth_date to the students table (Take a look at the id given).


INSERT INTO students(first_name, last_name, birth_date)VALUES
    ('Marc', 'Benichou', '1998-11-02'),
    ('Yoan', 'Cohen', '2010-12-03'),
    ('Lea', 'Benichou', '1987-07-27'),
    ('Amelia', 'Dux', '1996-04-07'),
    ('David', 'Grez', '2003-06-14'),
    ('Omer', 'Simpson', '1980-10-03');


-- 3. SELECT
-- (1) Fetch all of the data from the table.
select * from students;
-- (2) Fetch all of the students first_names and last_names.
select first_name,last_name from students;
-- (3) For the following questions, only fetch the first_names and last_names of the students.
--         Fetch the student which id is equal to 2.
select first_name,last_name from students where id = 2;
--         Fetch the student whose last_name is Benichou AND first_name is Marc.
select first_name,last_name from students where last_name ='Benichou' and first_name ='Marc';
--         Fetch the students whose last_names are Benichou OR first_names are Marc.
select first_name,last_name from students where last_name ='Benichou' or first_name ='Marc';
--         Fetch the students whose first_names contain the letter a.
select first_name,last_name from students where first_name LIKE '%a%';
--         Fetch the students whose first_names start with the letter a.
select first_name,last_name from students where first_name ILIKE 'a%';  -- so we can cover big letter A as well
--         Fetch the students whose first_names end with the letter a.
select first_name,last_name from students where first_name LIKE '%a';
--         Fetch the students whose second to last letter of their first_names are a (Example: Leah).
SELECT first_name, last_name from students
WHERE SUBSTRING(first_name from LENGTH(first_name) - 1 FOR 1) = 'a';
--         Fetch the students whose id’s are equal to 1 AND 3 .
SELECT first_name, last_name from students where id = 3 and id = 1;
-- (4) Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
SELECT * from students where birth_date >= DATE '2000-01-01'