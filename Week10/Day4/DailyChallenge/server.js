const express = require('express');
const app = express();
const port = 9000;
const fs = require('fs');
const path = require('path');
const dataPath = path.join(__dirname, 'data', 'users.json');


app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded());

app.post('/register', (req, res) => {
    const userData = req.body;
    console.log(userData)
    // Check if username or password already exist
    let users = [];

    // in case users.json is empty 
    if (fs.existsSync(dataPath)) {
        const fileData = fs.readFileSync(dataPath, 'utf8');
        if (fileData.trim() !== '') {
            users = JSON.parse(fileData);
        }
    }

    const isExistingUser = users.some(user => user.username === userData.username || user.password === userData.password);

    if (isExistingUser) {
        res.json({ message: 'error1' }); // User or password already exists
    } else {
        users.push(userData);

        fs.writeFileSync(dataPath, JSON.stringify(users, null, 2));

        res.json({ message: 'register' }); // User registered successfully
    }
});



app.post('/login', (req, res) => {
    const loginData = req.body;

    // Check if user exists
    const users = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
    const isUserRegistered = users.some(user => user.username === loginData.username && user.password === loginData.password);

    if (isUserRegistered) {
        res.json({ message: 'login' }); // User logged in successfully
    } else {
        res.json({ message: 'error2' }); // User not registered
    }
});



app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});