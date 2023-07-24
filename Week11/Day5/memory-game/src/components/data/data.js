// import data from './superheroes.json'
let data = require('./superheroes.json')
// console.log(data.superheroes)
data.superheroes.map(hero=>console.log("Hi",hero))