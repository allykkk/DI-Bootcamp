// 🌟 Exercice 4 : Volume of a sphere

// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:
const form = document.querySelector('form')


function calculateVolumn(radius) {
    return (4 / 3) * Math.PI * Math.pow(radius, 3)
}


function InputValidation(userInput) {
    try {
        return Number(userInput)
    }
    catch {
        return NaN
    }
}


form.addEventListener('submit', (event) => {
    event.preventDefault();
    const inputRadius = document.querySelector('#radius');
    const numberRadius = InputValidation(inputRadius.value);
    const calculatedVolume = calculateVolumn(numberRadius);

    const volumeInput = document.querySelector('#volume')
    volumeInput.value = isNaN(calculatedVolume) ? 'Please Input Number for Radius' : calculatedVolume.toFixed(2);
});