-- Daily challenge: Tables Relationships
-- # Part I
-- 1. Create 2 tables : Customer and Customer profile. They have a One to One relationship.
--     A customer can have only one profile, and a profile belongs to only one customer
--     The Customer table should have the columns : id, first_name, last_name NOT NULL
--     The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)

CREATE TABLE Customer
(
    id         SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name  VARCHAR(255) NOT NULL
);

CREATE TABLE CustomerProfile
(
    id          SERIAL PRIMARY KEY,
    isLoggedIn  BOOLEAN DEFAULT false,
    customer_id INTEGER UNIQUE,
    FOREIGN KEY (customer_id) REFERENCES Customer (id)
);

-- 2. Insert those customers
--     John, Doe
--     Jerome, Lalu
--     Lea, Rive

INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe'),
       ('Jerome', 'Lalu'),
       ('Lea', 'Rive');

-- 3. Insert those customer profiles, use subqueries
INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (true, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')),
       (false, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));



-- 4. Use the relevant types of Joins to display:
--      (1)The first_name of the LoggedIn customers
SELECT c.first_name, cp.isLoggedIn
from Customer c
         RIGHT JOIN CustomerProfile cp on c.id = cp.customer_id
WHERE isLoggedIn = TRUE;
--      (2)All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT c.first_name, cp.isLoggedIn
from Customer c
         LEFT JOIN CustomerProfile cp on c.id = cp.customer_id;
--      (3)The number of customers that are not LoggedIn
SELECT COUNT(*)
FROM CustomerProfile
WHERE isLoggedIn = FALSE;


-- # Part II:
-- 1. Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
CREATE TABLE Book
(
    book_id SERIAL PRIMARY KEY,
    title   VARCHAR(255) NOT NULL,
    author  VARCHAR(255) NOT NULL
);

-- 2. Insert those books :
--     Alice In Wonderland, Lewis Carroll
--     Harry Potter, J.K Rowling
--     To kill a mockingbird, Harper Lee
INSERT INTO Book(title, author)
VALUES ('Alice In Wonderland', 'Lewis Carroll'),
       ('Harry Potter', 'J.K Rowling'),
       ('To kill a mockingbird', 'Harper Lee');

-- 3. Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);
CREATE TABLE Student
(
    student_id SERIAL PRIMARY KEY,
    name       VARCHAR(255) NOT NULL UNIQUE,
    age        INTEGER CHECK (age <= 15)
);

-- 4. Insert those students:
--     John, 12
--     Lera, 11
--     Patrick, 10
--     Bob, 14
INSERT INTO Student (name, age)
VALUES ('John', 12),
       ('Lera', 11),
       ('Patrick', 10),
       ('Bob', 14);

-- 5. Create a table named Library, with the columns :
--     book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
--     student_id ON DELETE CASCADE ON UPDATE CASCADE
--     borrowed_date
--     This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
--     book_fk_id is a Foreign Key representing the column book_id from the Book table
--     student_fk_id is a Foreign Key representing the column student_id from the Student table
--     The pair of Foreign Keys is the Primary Key of the Junction Table

CREATE TABLE Library
(
    book_fk_id    INTEGER,
    student_fk_id INTEGER,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    FOREIGN KEY (book_fk_id) REFERENCES Book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_fk_id) REFERENCES Student (student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 6. Add 4 records in the junction table, use subqueries.
--
--     the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
--     the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
--     the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
--     the student named Bob, borrowed the book Harry Potter the on 12/08/2021

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
        (SELECT student_id FROM Student WHERE name = 'John'),
        '2022-02-15'),

       ((SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
        (SELECT student_id FROM Student WHERE name = 'Bob'),
        '2021-03-03'),

       ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
        (SELECT student_id FROM Student WHERE name = 'Lera'),
        '2021-05-23'),

       ((SELECT book_id FROM Book WHERE title = 'Harry Potter'),
        (SELECT student_id FROM Student WHERE name = 'Bob'),
        '2021-08-12');

-- 7. Display the data
--    (1) Select all the columns from the junction table
SELECT *
from Library;

--    (2) Select the name of the student and the title of the borrowed books
SELECT s.name, b.title
from Library
         JOIN Book b on Library.book_fk_id = b.book_id
         JOIN Student s on s.student_id = Library.student_fk_id;
--    (3) Select the average age of the children, that borrowed the book Alice in Wonderland
SELECT AVG(age) AS average_age
FROM Library
         JOIN Student ON Library.student_fk_id = Student.student_id
         JOIN Book ON Library.book_fk_id = Book.book_id
WHERE Book.title = 'Alice In Wonderland';
--     (4) Delete a student from the Student table, what happened in the junction table ?
DELETE from Student
WHERE name='Bob';
        --    Records related to Bob are deleted in Library as well.

