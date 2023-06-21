//🌟 Exercise 6 : Change the navbar

// 1. Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
const navBar = document.getElementById('navBar');
navBar.setAttribute('id', 'socialNetworkNavigation');

// 2. We are going to add a new <li> to the <ul>.

//    First, create a new <li> tag (use the createElement method).
const newLi = document.createElement('li');
//    Create a new text node with “Logout” as its specified text.
const logOut = document.createTextNode('Logout');
//    Append the text node to the newly created list node (<li>).
newLi.appendChild(logOut);
//    Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.</ul>
const ul = navBar.querySelector('ul');
ul.appendChild(newLi);

// 3. Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).
const firstLi = ul.firstElementChild;
const lastLi = ul.lastElementChild;

console.log(firstLi.textContent);
console.log(lastLi.textContent);