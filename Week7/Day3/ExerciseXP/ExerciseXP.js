// 🌟 Exercise 1 : List of people
const people = ["Greg", "Mary", "Devon", "James"];

// Part I - Review about arrays
// 1. Write code to remove “Greg” from the people array.
people.splice(people.indexOf("Greg"), 1);
// 2. Write code to replace “James” to “Jason”.
people[people.indexOf("James")] = "Jason";
// 3. Write code to add your name to the end of the people array.
people.push("Ally");
// 4. Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
console.log(people.indexOf("Mary"));
// 5. Write code to make a copy of the people array using the slice method. The copy should NOT include “Mary” or your name. 
const peopleCopy = people.slice(1, 3);
// 6. Write code that gives the index of “Foo”. Why does it return -1 ?
console.log(people.indexOf("Foo")); // because "Foo" doesn't exist in this array
// 7. Create a variable called last which value is the last element of the array.
const last = people[people.length - 1];
// Testing Part I
console.log(people);
console.log(peopleCopy);
console.log(last);


// Part II - Loops
// 1. Using a loop, iterate through the people array and console.log each person.
for (let person of people)
    console.log(person);
// 2. Using a loop, iterate through the people array and exit the loop after you console.log “Devon” . 
for (let person of people) {
    console.log(person);
    if (person === "Devon")
        break;
};

// -------------------------------------------------------------------------------
// 🌟 Exercise 2 : Your favorite colors
// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
console.log("***Exercise 2");
const colors = ["blue", "red", "green", "yellow", "purple"];
for (let index in colors) {
    console.log(`My #${Number(index) + 1} choice is ${colors[index]}.`)
}

// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus
const suffixes = ["st", "nd", "rd", "th", "th"];
for (let index in colors) {
    console.log(`My ${Number(index) + 1}${suffixes[index]} choice is ${colors[index]}.`)
}

// -------------------------------------------------------------------------------
// 🌟 Exercise 3 : Repeat the question
// 1.Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
// let userInput = prompt("Enter a number:");
// console.log(typeof userInput);  //prompt return value is string 

// 2. While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
let userInput;
do{
    userInput=Number(prompt("Enter a number:"));
}while(userInput<10);



// -------------------------------------------------------------------------------
// 🌟 Exercise 4 : Building Management
// 1. Copy and paste the above object to your Javascript file.
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}

// 2. Console.log the number of floors in the building.
console.log("***Exercise 4")
console.log(building.numberOfFloors)
// 3. Console.log how many apartments are on the floors 1 and 3.
console.log("Apartments on the 1st floor:", building.numberOfAptByFloor.firstFloor);
console.log("Apartments on the 3rd floor:", building.numberOfAptByFloor.thirdFloor);
// 4. Console.log the name of the second tenant and the number of rooms he has in his apartment. 
console.log("2nd Tenants:", building.nameOfTenants[1], "; number of rooms:", building.numberOfRoomsAndRent.dan[0])
// 5. Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];
if (sarahRent + davidRent > danRent)
    building.numberOfRoomsAndRent.dan[1] = 1200;
console.log("Dan's rent:", building.numberOfRoomsAndRent.dan[1]);


// -------------------------------------------------------------------------------
// 🌟 Exercise 5 : Family
// 1. Create an object called family with a few key value pairs.
const family = {
    father: "John",
    mother: "Emily",
    daughter: "Sophia",
    son: "James"
};
console.log("***Exercise 5")
// 2. Using a for in loop, console.log the keys of the object.
for (let key in family)
    console.log(key);

// 3. Using a for in loop, console.log the values of the object.
for (let key in family)
    console.log(family[key]);

// -------------------------------------------------------------------------------
// Exercise 6 : Rudolf
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}
console.log("***Exercise 6")
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
let sentence = "";
for (let [key, value] of Object.entries(details)) {
    sentence += key + " " + value + " ";
}
console.log(sentence)


// -------------------------------------------------------------------------------
// Exercise 7 : Secret Group
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
console.log("***Exercise 7")
names.sort();
const societyName = names.map(name => name[0]).join("");
console.log("Secret society's name:", societyName);