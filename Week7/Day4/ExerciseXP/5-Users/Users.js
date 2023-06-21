
// 1. Using Javascript:

//     Retrieve the div and console.log it
const container = document.getElementById('container');
console.log(container);
//     Change the name “Pete” to “Richard”.
const peteElement = document.querySelector('.list:nth-of-type(1) li:nth-of-type(2)');
peteElement.textContent = 'Richard';
//     Delete the second <li> of the second <ul>.
const secondUl = document.querySelector('.list:nth-of-type(2)');
const secondLi = secondUl.querySelector('li:nth-of-type(2)');
secondUl.removeChild(secondLi);
//     Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)
const allLists = document.querySelectorAll('.list');
allLists.forEach((list) => {
  const firstLi = list.querySelector('li:first-child');
  firstLi.textContent = 'Ally';
});
// 2. Using Javascript:

//     Add a class called student_list to both of the <ul>'s.
allLists.forEach((list) => {
  list.classList.add('student_list');
});
//     Add the classes university and attendance to the first <ul>.
const firstUl = document.querySelector('.list:first-of-type');
firstUl.classList.add('university', 'attendance');
// 3. Using Javascript:

//     Add a “light blue” background color and some padding to the <div>.
container.style.backgroundColor = 'lightblue';
container.style.padding = '15px';
//     Do not display the <li> that contains the text node “Dan”. 
const danLi = secondUl.querySelector('li:last-child');
danLi.style.display = 'none';
//     Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
peteElement.style.border = '2px solid black';
//     Change the font size of the whole body.
document.body.style.fontSize = '20px';
// 4. Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
if (container.style.backgroundColor === 'lightblue') {
  const userList = Array.from(document.querySelectorAll('.list li'));
  const users = userList.map((li) => li.textContent);
  alert(`Hello ${users[0]} and ${users[1]}`);
}