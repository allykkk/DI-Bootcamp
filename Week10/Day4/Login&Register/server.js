const express = require('express')
const knex = require('knex')
const app = express()

app.use(express.json());
app.use(express.urlencoded())

const db = knex({
    client: 'sqlite3',
    connection: {
        filename: './database.db',
    },
    useNullAsDefault: true,
})
    

// create table with knex
// db.schema.createTable('users', function (table) {
//     table.increments('id').primary();
//     table.string('firstName').notNullable();
//     table.string('lastName').notNullable();
//     table.string('email').notNullable().unique();
//     table.string('username').notNullable().unique();
//     table.string('password').notNullable();
//   })
//   .then(() => {
//     console.log('Table "users" created successfully');
//   })
//   .catch((error) => {
//     console.error('Error creating "users" table:', error);
//   });


app.post('/register', async (req, res) => {
    const { firstName, lastName, email, username, password } = req.body;

    try {
        // Insert the new user into the database
        await db('users').insert({ firstName, lastName, email, username, password });

        res.status(200).json({ message: 'User registered successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});


app.post('/login', async (req, res) => {
    const { username, password } = req.body;

    try {
        // Retrieve the user from the database based on the username and password
        const user = await db('users')
            .where({ username, password })
            .first();

        if (user) {
            res.status(200).json({ message: 'Login successful', user });
        } else {
            res.status(401).json({ error: 'Invalid credentials' });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});