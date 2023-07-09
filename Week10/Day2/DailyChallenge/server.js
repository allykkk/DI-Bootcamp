// Instructions

//     Use Express to create a few routes:
//         The route /aboutMe/:hobby sends the name of one hobby (ie. the value of the route parameter). If the parameter is not a string (ie. numbers or else), set the status to 404.
//         The route /pic : displays an HTML file with a picture of your choice.
//         The route /form: displays an HTML file.
//             Requirements:
//                 The HTML file must be in the public folder.
//                 The HTML file must contain a form to contact you.
//                 The form must contain the inputs email and message. (add some HTML form validations)
//             Output:
//                 You should get the data and display it on the browser at the route /formData.
//                 For example, “john@gmail.com sent you a message “Love your new website”.



const express = require('express')
const app = express()
const path = require('path');
const port = 5000

app.use(express.json())
app.use(express.urlencoded())

function IsOnlyLetters(str){
    const noNumbersRegex=/^([^0-9]*)$/;
    return noNumbersRegex.test(str);
}


app.get('/aboutMe/:hobby' , (req , res)=>{
    const { hobby } = req.params;
    if (IsOnlyLetters(hobby)) {
        return res.send(hobby);
        } 
    res.status(404).send('Invalid hobby parameter');
})


app.get('/pic' , (req , res)=>{
    res.sendFile(path.join(__dirname, 'public', 'picture.html'));
})

app.get('/form', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'form.html'));
  });

app.post('/formData', (req, res) => {
    console.log('formdata',req.body)
    const { email, message } = req.body;
    res.send(`${email} sent you a message: "${message}"`);
});

app.listen(port , ()=> console.log('> Server is up and running on port : ' + port))