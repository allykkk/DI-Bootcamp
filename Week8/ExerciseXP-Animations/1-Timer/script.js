// 1️⃣ Part I

// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.

setTimeout(() => {
    alert("Hello World");
}, 2000)

// 2️⃣ Part II

// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
const container = document.getElementById("container");

function addParagraph() {
    const paragraph = document.createElement("p");
    paragraph.textContent = "Hello World";
    container.appendChild(paragraph);
}

setTimeout(() => {
    addParagraph();
}, 2000);

// 3️⃣ Part III

// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.


const interval = setInterval(() => {
    const paragraphs = container.getElementsByTagName("p");
    if (paragraphs.length < 5) {
        addParagraph();
    } else {
        clearInterval(interval);
    }
}, 2000);


const clearButton = document.querySelector('#clear')
clearButton.addEventListener('click', () => {
    clearInterval(interval);
});