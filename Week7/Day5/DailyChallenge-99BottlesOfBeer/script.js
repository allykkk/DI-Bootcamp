const songSection = document.querySelector('#song')


function inputValidation(input) {
    const converted = parseInt(input);
    if (!converted && converted !== 0) {  // in case user input is 0 
        const errorMessage = document.createElement('p')
        errorMessage.textContent = 'Number only!';
        errorMessage.style.color = 'red';
        songSection.appendChild(errorMessage);
    }
    else {
        songSection.innerHTML = '';
    }
    return converted;// if converted is a number - truthy, otherwise return falsy
}

addEventListener("submit", (event) => {
    event.preventDefault();
    const bottleNumber = document.getElementById("bottblenum").value;
    const convertedNum = inputValidation(bottleNumber)
    if (convertedNum) { // when input is actual valid number 

    }

});

