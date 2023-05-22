-- Daily challenge : SQL Puzzle

CREATE TABLE FirstTab (
     id integer,
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer
);

INSERT INTO SecondTab VALUES
(5),
(NULL);

SELECT * FROM SecondTab;


-- Questions

-- Q1. What will be the OUTPUT of the following statement?
SELECT COUNT(*)
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
--     0, In SQL, comparisons with NULL always result in UNKNOWN. As a result, no rows satisfy the query condition, and the count is 0.

-- Q2. What will be the OUTPUT of the following statement?
SELECT COUNT(*)
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
--     2

-- Q3. What will be the OUTPUT of the following statement?
SELECT COUNT(*)
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );
--     0

-- Q4. What will be the OUTPUT of the following statement?
SELECT COUNT(*)
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
--     2
