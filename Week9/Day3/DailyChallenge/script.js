// Instructions

//     Use this Giphy API Random documentation. Use this API Key : hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
//     In the HTML file, add a form, containing an input and a button. This input is used to fetch gif depending on a specific category.
//     In the JS file, create a program to fetch one random gif depending on the search of the user (ie. If the search is “sun”, append on the page one gif with a category of “sun”).
//     The gif should be appended with a DELETE button next to it. Hint : to find the URL of the gif, look for the sub-object named “images” inside the data you receive from the API.
//     Allow the user to delete a specific gif by clicking the DELETE button.
//     Allow the user to remove all of the GIFs by clicking a DELETE ALL button.


const apiKey = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';

async function getOneGif(searchTerm) {
    const originalUrl = 'https://api.giphy.com/v1/gifs/random'
    const url = `${originalUrl}?api_key=${apiKey}&tag=${searchTerm}&limit=1`
    console.log(url)
    try {
        const response = await fetch(url);
        const data = await response.json();
        const gifUrl = data.data.images.original.url;
        return gifUrl
    } catch (error) {
        console.log('Error fetching GIF:', error);
    }
}
console.log(getOneGif('dog'))


function addGif(url) {
    const container = document.getElementById('gifContainer');
    const gifDiv = document.createElement('div');
    gifDiv.classList.add('img-div')
    gifDiv.innerHTML = `<img src="${url}" alt="GIF">
    <button class="deleteBtn">Delete</button>`;
    container.appendChild(gifDiv);
}

async function submitHandler(event) {
    event.preventDefault();
    const searchInput = document.getElementById('searchInput')
    const searchTerm = searchInput.value.trim();
    if (searchTerm !== "") {
        const gifUrl = await getOneGif(searchTerm);
        addGif(gifUrl);
        searchInput.value = "";
    }
    else {
        alert('Invalid Input')
    }
}

function deleteGif(event) {
    if (event.target.classList.contains("deleteBtn")) {
        const gifElement = event.target.parentNode;
        gifElement.remove();
    }
}

function deleteAllGifs() {
    const container = document.getElementById("gifContainer");
    while (container.firstChild) {
        container.firstChild.remove();
    }
}

const gifForm = document.getElementById('gifForm');
const deleteAllBtn = document.getElementById("deleteAllBtn");

gifForm.addEventListener('submit', submitHandler);
deleteAllBtn.addEventListener("click", deleteAllGifs);
document.addEventListener("click", deleteGif);