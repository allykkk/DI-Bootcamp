// 🌟 Exercise 2 : Ternary operator

// function winBattle() {
//     return true;
// }


// Transform the winBattle() function to an arrow function.
// Create a variable called experiencePoints.
// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
// Console.log the experiencePoints variable.

console.log("Exercise 2");
const winBattle = () => true;
const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints);

// ---------------------------------------
// 🌟 Exercise 3 : Is it a string ?

// Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
// Check out the example below to see the expected output
console.log("Exercise 3");

const isString = (value) => {
    return (typeof value === 'string')
};

console.log(isString('hello'));
//true
console.log(isString([1, 2, 4, 0]));
//false


// ---------------------------------------
// 🌟 Exercise 4 : Find the sum

// Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.
console.log("Exercise 4");

const sum = (a, b) => a + b;
console.log(sum(1, 2))


// ---------------------------------------
// 🌟 Exercise 5 : Kg and grams
// Instructions

// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)

//     First, use function declaration and invoke it.
//     Then, use function expression and invoke it.
//     Write in a one line comment, the difference between function declaration and function expression.
//     Finally, use a one line arrow function and invoke it.
console.log("Exercise 5");

// Function Declaration
function convertToGramsDeclaration(weightInKg) {
    return weightInKg * 1000;
}

console.log(convertToGramsDeclaration(2));

// Function Expression
const convertToGramsExpression = function (weightInKg) {
    return weightInKg * 1000;
};

console.log(convertToGramsExpression(2));

// 📝 Answer: function declarations are hoisted, they can be called before they are defined in the code.

// One-Line Arrow Function
const convertToGramsArrow = weightInKg => weightInKg * 1000;
console.log(convertToGramsArrow(2));


// ---------------------------------------
// 🌟 Exercise 6 : Fortune teller


// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."

(function (numberOfChildren, partnerName, location, jobTitle) {
    const sentence = `You will be a ${jobTitle} in ${location}, and married to ${partnerName} with ${numberOfChildren} kids.`;
    document.getElementById('exercise6').textContent = sentence;
})(2, 'Someone', 'Somewhere', 'Random job');


// ---------------------------------------
// 🌟 Exercise 7 : Welcome

// John has just signed in to your website and you want to welcome him.

//     Create a Navbar in your HTML file.
//     In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
//     The function should add a div in the nabvar, displaying the name of the user and his profile picture.

(function (userName) {
    const userInfoDiv = document.getElementById('exercise7');

    // Set user name
    const userNameElement = document.createElement('span');
    userNameElement.textContent = userName;

    // Set user profile picture
    const profilePictureElement = document.createElement('img');
    profilePictureElement.src = 'https://res.cloudinary.com/crunchbase-production/image/upload/c_thumb,h_256,w_256,f_auto,g_faces,z_0.7,q_auto:eco,dpr_1/v1397181962/3f786f068307ab5fe606473b67c0817e.jpg';
    profilePictureElement.alt = 'Profile Picture';

    // Append elements to user-info div
    userInfoDiv.appendChild(userNameElement);
    userInfoDiv.appendChild(profilePictureElement);
})('John');


