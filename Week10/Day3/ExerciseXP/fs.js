// Exercise 1 : Reading from a file in Node.JS
// Instructions

//     Create a text file and write something inside (example: ‘Some Text To See’)
//     Create an fs.js file, and inside use the Node JS File System to read the text file and console.log the output in the terminal


const fs = require('fs')


fs.readFile('data.txt', 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
        return
    }
    console.log(data)
});

// Exercise 2 : Writing files with Node JS
// 1. Create an fs.js file, and use the Node js File System to create a new text file and write to it.
const content = 'Bla bla'
fs.writeFile('newFile.txt', content, 'utf-8', (err) => {
    if (err) {
        console.log(err);
        return
    }

    console.log("Created a new file with content.")
})

// 2. Use the Node js File System to append some other text to the text file. (Example:”Buy orange juice”)
fs.appendFile('newFile.txt', '\nBuy orange juice', 'utf8', (err) => {
    if (err) {
        console.log(err);
        return
    }
    console.log("Added new content")
})


// 3.Use the Node js File System to delete the file.
fs.unlink('newFile.txt',(err) => {
    if (err) {
        console.log(err);
        return
    }
    console.log("File deleted")
})