const express = require('express');
const app = express()
const port = 5000
const { items, categories, searchByCategory, searchByTitle } = require('./rss');
const { urlencoded } = require('body-parser');

app.set('view engine', 'ejs');
app.set('views', __dirname + '/public/pages');

app.use(express())
app.use(urlencoded())


app.get('/', async (req, res) => {
    try {
        res.render('index', { items: await items });
    } catch (error) {
        console.error(error);
        res.render('index', { items: [] });
    }
})

app.get('/search', async (req, res) => {
    res.render('search', { retrievedCategories: await categories, items: [] })
})


app.post('/search/title', async (req, res) => {
    res.render('search', { items: await searchByTitle(req.body.title), retrievedCategories: await categories });
});


app.post('/search/category', async (req, res) => {
    res.render('search', { items: await searchByCategory(req.body.category), retrievedCategories: await categories });
});




app.listen(port, () => console.log(`listening on port ${port}!`));