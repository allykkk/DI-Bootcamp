// 🌟 Exercise 1 : Comparison

// Instructions

//     Create a function called compareToTen(num) that takes a number as an argument.
//     The function should return a Promise:
//         the promise resolves if the argument is less than or equal to 10
//         the promise rejects if argument is greater than 10.

//In the example, the promise should reject
compareToTen(15)
    .then(result => console.log("15", result))
    .catch(error => console.log("15", error.message));

//In the example, the promise should resolve
compareToTen(8)
    .then(result => console.log("8", result))
    .catch(error => console.log("8", error.message));


function compareToTen(num) {
    return new Promise((resolve, reject) => {
        if (num <= 10)
            resolve("Smaller or equal to 10")
        else
            reject(new Error('Bigger than 10!'))
    })
};



// 🌟 Exercise 2 : Promises
// Instructions

// Create a promise that resolves itself in 4 seconds and returns a “success” string.
const p = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Success')
    }, 4000);
});

p.then(result => console.log("Exercise2", result));


// 🌟 Exercise 3 : Resolve & Reject

// Instructions

//     Use Promise.resolve(value) to create a promise that will resolve itself with a value of 3.


p2 = new Promise((resolve, reject) => {
    resolve(3)
});

p2.then(result => console.log("Exercise3-1 ", result));

//     Use Promise.reject(error) to create a promise that will reject itself with the string “Boo!”

p3 = new Promise((resolve, reject) => {
    reject(new Error('Boo'))
});

p3.catch(err => console.log("Exercise3-2 ", err.message));

