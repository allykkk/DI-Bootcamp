let Parser = require('rss-parser');
let parser = new Parser();


async function retrieveFactsFromRSS() {
    try {
        let feed = await parser.parseURL('https://thefactfile.org/feed/');
        return feed.items // array that consists of item object 
    } catch (error) {
        console.log("Error: " + error);
        return []
    }
}
const items = retrieveFactsFromRSS()


async function searchByTitle(searchInput) {
    const body = []
    for (item of await items) {
        if (item.title.toLowerCase().indexOf(searchInput.toLowerCase()) != -1)
            body.push(item)
    }
    return body
}

async function getAllCategories() {
    const categories = []
    for (item of await items) {
        for (category of item.categories)
            if (!categories.includes(category))
                categories.push(category)
    }
    return categories
}
const categories = getAllCategories()


async function searchByCategory(searchInput) {
    const body = []
    for (item of await items) {
        if (item.categories.includes(searchInput)) {
            console.log("Found one")
            body.push(item)
        }
    }
    return body
}

module.exports = { items, categories, searchByCategory, searchByTitle }