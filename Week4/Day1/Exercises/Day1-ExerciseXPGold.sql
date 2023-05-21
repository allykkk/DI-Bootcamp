-- Exercise 1 : Bootcamp
-- Instructions
--
-- Continuation of the Exercise XP
-- Select
--
-- For the following questions, you have to fetch the first_names, last_names and birth_dates of the students.
--
--     Fetch the first four students. You have to order the four students alphabetically by last_name.
--     Fetch the details of the youngest student.
--     Fetch three students skipping the first two students.
--

SELECT * from students ORDER BY last_name LIMIT 4;

SELECT * from students ORDER BY birth_date DESC LIMIT 1;

SELECT * from students OFFSET 2 LIMIT 3;