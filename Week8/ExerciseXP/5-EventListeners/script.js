// Exercise 5 : Event Listeners
// Instructions

// Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
// Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.

const container = document.querySelector('#container');


// Click 
container.addEventListener('click', () => {
    container.style.backgroundColor = 'green';
});

// Mouseover
container.addEventListener('mouseover', () => {
    container.style.color = "red";
});

// Mouseout 
container.addEventListener('mouseout', () => {
    container.style.color = "white";
});

//Dbclick
container.addEventListener('dblclick', () => {
    container.style.fontSize = "24px";
});