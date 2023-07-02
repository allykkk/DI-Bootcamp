// Exercise 1 : Express & JSON
// Instructions

//     Create a public folder containing two files : index.html and script.js
//     Outside of the public folder, create a file named server.js.
//     In the server.js file, create an express server. Create a GET request to the route /users.
//     The handler function of the /users route should send a stringified version of this javascript object const user = {firstname: 'John',lastname: 'Doe'}.
//     In the script.js file, fetch the server at the route /users and get the response.
//     The response should be the JSON Object. Console.log this object and display it on the DOM.

const express = require('express');
const app = express();
const port = 3000;

const user = { firstname: 'John', lastname: 'Doe' };

app.get('/users', (req, res) => {
    const userStr = JSON.stringify(user);
    res.send(userStr);
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});