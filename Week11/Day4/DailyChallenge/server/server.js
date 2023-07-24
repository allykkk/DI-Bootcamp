const express = require('express')
const cors = require('cors');
const app = express()
const port = 5000

app.use(cors())
app.use(express.json())
app.use(express.urlencoded())


app.get('/api/hello', (req, res) => {

    res.send('Hello From Express')

})

app.post('/api/world', (req, res) => {
    const userInput = req.body.value
    console.log(`{post: '${userInput}'}`)
    res.send(`I received your POST request. This is what you sent me: ${userInput}`);
})

app.listen(port, () => console.log('> Server is up and running on port : ' + port))