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


async function formDataHandler(event,form,route) {
    console.log("Entered form data handler!")
    event.preventDefault(); 
    console.log(form)
    const formData = new FormData(form);
    console.log('formData',formData)
    const requestBody = {};

    // Loop through each input field and retrieve its value
    for (const [key, value] of formData.entries()) {
        console.log('k',key);
        console.log('v',value);
        requestBody[key] = value;
    }
    console.log(requestBody)
    try {
        const response = await fetch(`/${route}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        // Handle the response from the server
        if (response.ok) {
            // Successful login
            const data = await response.json();
            console.log('Logged in:', data);
        } else {
            console.log('Form handling Failed');
        }
    } catch (error) {
        // Error during the request
        console.log('Error during handling:', error);
    }
}





const loginForm = document.getElementById('login-form');
const loginBtn = document.getElementById('loginBtn');
// Listen for changes in the login form inputs
loginForm.addEventListener('input', () => {
    checkInputs(loginForm, loginBtn)
});

loginForm.addEventListener('submit', (event) => {
    console.log('Submitted')
    formDataHandler(event, loginForm,'login')
    .then(()=>console.log('Sucess!'))
    .catch((error) => {
        console.error('Error during login:', error);
    })
});


const registerForm = document.getElementById('register-form');
const registerBtn = document.getElementById('registerBtn');
// Listen for changes in the register form inputs
registerForm.addEventListener('input', () => {
    checkInputs(registerForm, registerBtn)
});

registerForm.addEventListener('submit', (event) => {
    console.log('Submitted')
    formDataHandler(event, registerForm,'register')
    // .then(()=>console.log("Sucess!"))
    // .catch((error) => {
    //     console.error('Error during login:', error);
    // })
});