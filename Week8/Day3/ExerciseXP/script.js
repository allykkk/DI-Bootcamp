//🌟 Exercise 1 : Colors
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
console.log('*Exercise1*');

// 1. Write a JavaScript program that displays the colors in the following order : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…
colors.forEach((color, index) => {
    console.log(`${index + 1}# choice is ${color}.`)
});

// 2. Check if at least one element of the array is equal to the value “Violet”. If yes, console.log("Yeah"), else console.log("No...")
if (colors.includes("Violet"))
    console.log("Yeah");
else
    console.log("No...");


// ---------------------------------------------
//🌟 Exercise 2 : Colors #2
// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];   // same as the colors above 
const ordinal = ["th", "st", "nd", "rd"];
console.log('*Exercise2*')
colors.forEach((color, index) => {
    const actualIndex = index >= 3 ? 0 : index + 1
    console.log(`${index + 1}${ordinal[actualIndex]} choice is ${color}.`)
});

// ---------------------------------------------
//🌟 Exercise 3 : Analyzing
// Analyze these pieces of code before executing them. What will be the outputs ?
console.log('*Exercise3*')

// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);  // 📝 ['bread', 'carrot', 'potato', 'chicken', 'apple', 'orange']

// ------2------
const country = "USA";
console.log([...country]);  // 📝  ['U', 'S', 'A']

// ------Bonus------
let newArray = [...[, ,]];
console.log(newArray);    // 📝  [undefined, undefined]



// ---------------------------------------------
//🌟 Exercise 4 : Employees

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
{ firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
{ firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
{ firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
{ firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
{ firstName: 'Wes', lastName: 'Reid', role: 'Instructor' },
{ firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor' }];

console.log('*Exercise4*');


// 1. Using the map() method, push into a new array the firstname of the user and a welcome message. You should get an array that looks like this : 
// const welcomeStudents = ["Hello Bradley", "Hello Chloe", "Hello Jonathan", "Hello Michael", "Hello Robert", "Hello Wes", "Hello Zach"]

const welcomeStudents = users.map(user => 'Hello ' + user['firstName']);
console.log(welcomeStudents);

// 2. Using the filter() method, create a new array, containing only the Full Stack Residents.

const fullStackStudents = users.filter(user => {
    return user['role'] === 'Full Stack Resident'
});
console.log(fullStackStudents)


// 3. Bonus : Chain the filter method with a map method, to return an array containing only the lastName of the Full Stack Residents.
const lastName = users
    .filter(user => {
        return user['role'] === 'Full Stack Resident'
    })
    .map(user => user['lastName']);
console.log(lastName);


// Exercise 5 is missing from the ExerciseXP page 
// ---------------------------------------------
//🌟 Exercise 6 : Star Wars
const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
console.log('*Exercise6*');

const epicString = epic.reduce((a, b) => a + ' ' + b);
console.log(epicString);


// ---------------------------------------------
//🌟 Exercise 7 : Employees #2
console.log('*Exercise7*');

const students = [{ name: "Ray", course: "Computer Science", isPassed: true },
{ name: "Liam", course: "Computer Science", isPassed: false },
{ name: "Jenner", course: "Information Technology", isPassed: true },
{ name: "Marco", course: "Robotics", isPassed: true },
{ name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
{ name: "Jamie", course: "Big Data", isPassed: false }];

// 1. Using the filter() method, create a new array, containing the students that passed the course.
passedStidents = students.filter((student) => {
    return student['isPassed'] === true
});
console.log(passedStidents)

// 2. Bonus : Chain the filter method with a forEach method, to congratulate the students with their name and course name (ie. “Good job Jenner, you passed the course in Information Technology”, “Good Job Marco you passed the course in Robotics” ect…)
congratMessage = students
    .filter((student) => {
        return student['isPassed'] === true
    })
    .forEach((student) => {
        console.log(`Good job ${student['name']}, you passed the course in ${student['course']}!`)
    });