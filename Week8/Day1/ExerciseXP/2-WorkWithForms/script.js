// 🌟 Exercise 2 : Work with forms


// 1. Retrieve the form and console.log it.
const form = document.querySelector('form');
console.log(form);


// Retrieve the inputs by their id and console.log them.
const firstName = document.getElementById('fname');
const lastName = document.getElementById('lname');

console.log(firstName);
console.log(lastName);


// Retrieve the inputs by their name attribute and console.log them.
const firstNameByName = document.querySelector('input[name="firstname"]');
const lastNameByName = document.querySelector('input[name="lastname"]');

console.log(firstNameByName);
console.log(lastNameByName);

// When the user submits the form (ie. submit event listener)
//     use event.preventDefault(), why ?
//     get the values of the input tags,
//     make sure that they are not empty,
//     create an li per input value,
//     then append them to a the <ul class="usersAnswer"></ul>, below the form.

form.addEventListener('submit', (event) => {
    event.preventDefault();
    //tells the user agent that if the event does not get explicitly handled, its default action should not be taken as it normally would be.
    const firstNameValue = firstName.value;
    const lastNameValue = lastName.value;
    const ul = document.querySelector('.usersAnswer');
    // clear the content for resubmit  
    ul.innerHTML = '';

    if (firstNameValue.trim() !== '' && lastNameValue.trim() !== '') {
        const firstLi = document.createElement('li');
        firstLi.textContent = firstNameValue;
        ul.appendChild(firstLi);

        const secondLi = document.createElement('li');
        secondLi.textContent = lastNameValue;
        ul.appendChild(secondLi);
    }

    else {
        const ErrorLi = document.createElement('li');
        ErrorLi.textContent = 'Please check your input'
        ul.appendChild(ErrorLi);
    }
})