// formType is login or register 
// Function to send message according to login/register status
function addMessage(formType, message) {
    const messageDiv = document.getElementById(`${formType}-message`)
    messageDiv.innerHTML = ''
    const messageP = document.createElement('p')
    messageP.innerText = message
    messageDiv.appendChild(messageP)
}


// Function to check if any input field is empty
function checkInputs(form, button) {
    let areInputsEmpty = false;

    // Loop through each input within the form
    for (const input of form.elements) {
        if (input.tagName === 'INPUT' && input.value.trim() === '') {
            areInputsEmpty = true;
            break;
        }
    }

    // Disable the login button if any input is empty
    button.disabled = areInputsEmpty;
}


// Handing Login Form
const loginForm = document.getElementById('login-form');
const loginBtn = document.getElementById('loginBtn');

// Listen for changes in the login form inputs
loginForm.addEventListener('input', () => {
    checkInputs(loginForm, loginBtn)
});

loginForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "username": username,
            "password": password,
        })
    })
        .then(response => {
            if (response.ok) return response.json();
            else throw new Error('Error: ', +response.status);
        })
        .then(data => {
            console.log(data)
            message = `Ok Hello your username is ${data.user.username}`
            addMessage('login', message)
        })
        .catch(error => {
            console.error('Error:', error);
            message = 'Not OK Username Or Password does not exist'
            addMessage('login', message)
        });

});


// Handling register form 

async function formDataHandler(event, form, route) {
    event.preventDefault();
    const formData = new FormData(form);
    const requestBody = {};

    formData.forEach(function (value, key) {
        requestBody[key] = value;
    });
    try {
        const response = await fetch(`/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        // Handle the response from the server
        const data = await response.json();
        if (response.ok) {
            message = `Okay Hello ${requestBody.firstName} ${requestBody.lastName}. Your ID is ${data.userId[0]}`
        } else {
            message = data.error
        }
        addMessage('register', message)
    } catch (error) {
        // Error during the request
        console.log('Error during handling:', error);
    }
}


const registerForm = document.getElementById('register-form');
const registerBtn = document.getElementById('registerBtn');
// Listen for changes in the register form inputs
registerForm.addEventListener('input', () => {
    checkInputs(registerForm, registerBtn)
});

registerForm.addEventListener('submit', (event) => {
    formDataHandler(event, registerForm, 'register')
});