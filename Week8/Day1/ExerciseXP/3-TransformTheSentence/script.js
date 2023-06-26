//🌟 Exercise 3 : Transform the sentence

// 1. Declare a global variable named allBoldItems.
let allBoldItems;

// 2. Create a function called getBoldItems() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
function getBoldItems() {
    allBoldItems = document.querySelectorAll('p strong'); //NodeList
}

// function getBoldItems() { // HTMLCollection
//     var paragraph = document.getElementsByTagName('p')[0]; 
//     allBoldItems = paragraph.getElementsByTagName('strong');
//   }

// make sure allBoldItems is usable for the following tasks
getBoldItems();

// 3. Create a function called highlight() that changes the color of all the bold text to blue. 
function highlight() {
    allBoldItems.forEach(item => item.style.color = 'blue');
}

// highlight();

// 4. Create a function called returnItemsToDefault() that changes the color of all the bold text back to black. 
function returnItemsToDefault() {
    allBoldItems.forEach(item => item.style.color = 'black');
}

// 5. Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function returnItemsToDefault() on mouseout (ie. when the mouse pointer is moved out of the paragraph).
const paragraph = document.querySelector('p')

paragraph.addEventListener('mouseover', highlight);

paragraph.addEventListener('mouseout', returnItemsToDefault);