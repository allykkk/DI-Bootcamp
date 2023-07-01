// Part I

// Create a file named main.js that contains a variable const largeNumber = 356; and export the module.

// Use the exported module in a script.js file.

// In the script.js file declare a variable const b = 5; and use it to output the sum of the imported module + b

const main = require('./main');
const b = 5;

const result = b + main.largeNumber
console.log(result);


// Part II:

// Before starting the exercises, check out the lesson named Node.js Application in the Course Notes.
//     In the script.js file create a server using the http module (require('http')).
//     Create a server instance and bind it at port 3000. Therefore your server should run on http://localhost:3000/. When the server run, you should console.log("I'm listening") in the terminal.
//     Set the response header to res.setHeader('Content-Type', 'text/html')(look at this tutorial- Part named “Serving HTML)
//     Respond (res.end) with a HTML paragraph saying "My Module is <result from Part I>", and an HTML <h1> saying “Hi there at the frontend”
const http = require('http');


const server1 = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/html');
    res.writeHead(200);
    res.end(`<html><body>
    <p>My Module is:<p>
    <p>${result}<p>
    <h1>Hi there at the frontend</h1>
    </body></html>`);
});


server1.listen(3000, () => {
    console.log("I am listening....")
})



// Part III:

//     In the main.js, create a function that returns the current date and time. Export the module.
//     Use the exported module in a script.js file.
//     Create a server with http and set the response header to 'text/html'. Respond with an HTML paragraph that outputs the current date and time from the exported module.
//     Your server should run on http://localhost:8080/

const dateTime = main.currentTime();
const server2 = http.createServer((req, res) => {
    res.write(`The date and time are currently: ${dateTime}`);
    res.end();
});

server2.listen(8080, () => {
    console.log('Server 2 is running...');
});
