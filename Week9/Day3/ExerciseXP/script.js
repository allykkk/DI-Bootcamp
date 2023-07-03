// 🌟 Exercise 1 : Giphy API

// Create a program to retrieve the data from the API URL provided above.
// Use the fetch() method to make a GET request to the Giphy API and Console.log the Javascript Object that you receive.
// Make sure to check the status of the Response and to catch any occuring errors.

const url =
    'https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';


async function getData(url) {
    try {
        const response = await fetch(url)
        const data = await response.json()
        if (response.status === 200) {
            console.log('Success', data)
        }
        else {
            console.log('Server Error', data.error.message)
        }
    } catch (error) {
        console.log('Fetch Error', error)
    }

}

getData(url)


// 🌟 Exercise 2 : Giphy API
// Instructions

//     Read carefully the documention to understand all the possible queries that the URL accept.
//     Use the Fetch API to retrieve 10 gifs about the “sun”. The starting position of the results should be 2.
//     Make sure to check the status of the Response and to catch any occuring errors.
//     Console.log the Javascript Object that you receive.

const searchTerm = 'sun';
const startingPosition = 2;
const limit = 10;

const url2 =
    `https://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&offset=${startingPosition}&limit=${limit}`;

getData(url2)



// 🌟 Exercise 3 : Async function
// Instructions

// Improve the program below :

// fetch("https://www.swapi.tech/api/starships/9/")
//     .then(response => response.json())
//     .then(objectStarWars => console.log(objectStarWars.result));

//     Create an async function, that will await for the above GET request.
//     The program shouldn’t contain any then() method.
//     Make sure to check the status of the Response and to catch any occuring errors.

async function getSwapiData() {
    const url = 'https://www.swapi.tech/api/starships/9/'
    try {
        const response = await fetch(url);
        const data = await response.json();
        if (response.status === 200) {
            console.log('Success', data.result)
        }
        else {
            console.log('Server Error', data.error.message)
        }
    } catch (error) {
        console.log('Fetch Error', error)
    }

}

getSwapiData();


// 🌟 Exercise 4: Analyze
// Instructions

// Analyse the code provided below - what will be the outcome?

function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();
// calling
// in 2 s , resolved 
