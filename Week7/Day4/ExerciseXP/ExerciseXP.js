// 🌟 Exercise 1 : Find the numbers divisible by 23
// Create a function call displayNumbersDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.
// Bonus: Add a parameter divisor to the function.

function displayNumbersDivisible(range, divisor) {
    sum = 0
    for (let i = 0; i < range; i++) {
        if (i % divisor === 0) {
            console.log(i);
            sum += i;
        };
    }
    console.log("Sum:", sum)
};
console.log('***Exercise 1***')
displayNumbersDivisible(500, 23)

// ---------------------------------------------------------------------------
//🌟 Exercise 2 : Shopping List
const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

console.log('***Exercise 2***');
// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
let shoppingList = ['banana', 'orange', 'apple'];

// Create a function called myBill() that takes no parameters.
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1.

function myBill(shoppingList) {
    let bill = 0;
    for (const item of shoppingList) {
        if (item in stock && stock[item] > 0) {
            bill += prices[item];
            stock[item] -= 1;
        }
        else {
            console.log("Shopping failed for item: " + item);
            break;
        }
    };
    return console.log("Total bill:", bill);
}

myBill(shoppingList)


// ---------------------------------------------------------------------------
// Exercise 3 : What’s in my wallet ?
// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :

//     an item price
//     and an array representing the amount of change in your pocket.

// In the function, determine whether or not you can afford the item.

//     If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
//     If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
console.log('***Exercise 3***')
// value of each type of coins
const currency = [0.25, 0.10, 0.05, 0.01]

function walletSum(array) {
    let sum = 0;
    for (let index in array) {
        sum += array[index] * currency[index];
    }
    return sum;
}

function changeEnough(itemPrice, amountOfChange) {
    const sum = walletSum(amountOfChange);
    return console.log(itemPrice <= sum);
}

//Tesing cases 
changeEnough(14.11, [2, 100, 0, 0])
changeEnough(0.75, [0, 0, 20, 5])

// ---------------------------------------------------------------------------
// 🌟 Exercise 4 : Vacations Costs
console.log('***Exercise 4***')
// 1. Define a function called hotelCost().
//     It should ask the user for the number of nights they would like to stay in the hotel.
//     If the user doesn’t answer or if the answer is not a number, ask again.
//     The hotel costs $140 per night. The function should return the total price of the hotel. 

function checkValidInput(question) {
    let validInput = false;
    while (!validInput) {
        let userIpnut = prompt(question);
        // since prompt returns string, we need first check if string is null or empty 
        if (userIpnut === null || userIpnut.trim() === "") continue;
        return userIpnut;
    }
}

function checkValidNumber(question) {
    let validInput = false;
    let parsedNumber;

    while (!validInput) {
        const userInput = checkValidInput(question);
        // try convert the userinput to number 
        parsedNumber = parseInt(userInput);
        if (isNaN(parsedNumber)) continue;
        validInput = true;
    }
    return parsedNumber;
}



function hotelCost() {
    let numberOfNights = checkValidNumber("Enter the number of nights you would like to stay in the hotel:");
    const hotelRate = 140;
    const totalCost = numberOfNights * hotelRate;
    // console.log("Total Hotel Cost:", totalCost)
    return totalCost;
}



// 2. Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
//     “London”: 183$
//     “Paris” : 220$
//     All other destination : 300$ 
function planeRideCost() {
    const ticketprice = {
        London: 183,
        Paris: 220,
        Others: 300
    }
    let destination = checkValidInput("Enter your plane destination:")
    if (destination.toLowerCase() === 'london') return ticketprice['London'];
    if (destination.toLowerCase() === 'paris') return ticketprice['Paris'];
    else return ticketprice['Others'];
}
// testing:
// console.log(planeRideCost())

// 3. Define a function called rentalCarCost().
//     It should ask the user for the number of days they would like to rent the car.
//     If the user doesn’t answer or if the answer is not a number, ask again.
//     Calculate the cost to rent the car. The car costs $40 everyday.
//         If the user rents a car for more than 10 days, they get a 5% discount.
//     The function should return the total price of the car rental. 
function rentalCarCost() {
    const costPerDay = 40;
    let rentalDays = checkValidNumber("Enter the number of days you would like to rent the car:");
    let rentalCost = rentalDays * costPerDay;
    if (rentalDays >= 10) rentalCost *= 0.95;
    // console.log("Rental Cost: ", rentalCost);
    return rentalCost;
}


// 4. Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().
function totalVacationCost() {
    const hotelCostValue = hotelCost();
    const planeRideCostValue = planeRideCost();
    const rentalCarCostValue = rentalCarCost();
    const totalCost = hotelCostValue + planeRideCostValue + rentalCarCostValue;

    console.log("The car cost: $" + rentalCarCostValue + ", the hotel cost: $" + hotelCostValue + ", the plane tickets cost: $" + planeRideCostValue + ".");
    console.log("Total cost: $", totalCost);
    return totalCost;
}

totalVacationCost();
