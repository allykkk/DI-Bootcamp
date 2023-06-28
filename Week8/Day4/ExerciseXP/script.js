//🌟 Exercise 1 : Location
console.log("*Exercise1*")

const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const { name, location: { country, city, coordinates: [lat, lng] } } = person;

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);

// Analyze the code below. What will be the output?
// 📝 I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)


// --------------------------------------------------------
// 🌟 Exercise 2: Display Student Info

// Using the code above, destructure the parameter inside the function and return a string as the example seen below:
// output : 'Your full name is Elie Schoppik'

function displayStudentInfo(objUser) {
    const { first, last } = objUser;
    return `Your full name is ${first} ${last}`;
}

displayStudentInfo({ first: 'Elie', last: 'Schoppik' });

console.log("*Exercise2*")
console.log(displayStudentInfo({ first: 'Elie', last: 'Schoppik' }))


// --------------------------------------------------------
// 🌟 Exercise 3: User & id
console.log("*Exercise3*")
const users = { user1: 18273, user2: 92833, user3: 90315 }


// Using methods taught in class, turn the users object into an array:
// Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]
// FYI : The number is their ID number.
const usersArray = Object.entries(users);
console.log(usersArray);



// Modify the outcome of part 1, by multipling the user’s ID by 2.
// Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]
const modifiedArray = usersArray.map(([key, value]) => [key, value * 2]);
console.log(modifiedArray)


// --------------------------------------------------------
// Exercise 4 : Person class
console.log("*Exercise4*")

class Person {
    constructor(name) {
        this.name = name;
    }
}

const member = new Person('John');
console.log(typeof member);

// Analyze the code below. What will be the output?
// 📝 object


// --------------------------------------------------------
// 🌟 Exercise 5 : Dog class
console.log("*Exercise5*")

class Dog {
    constructor(name) {
        this.name = name;
    }
};

// 1. Analyze the options below. Which constructor will successfully extend the Dog class?

// // 1
// class Labrador extends Dog {
//     constructor(name, size) {
//         this.size = size;
//     }
// };

// 2
class Labrador extends Dog {
    constructor(name, size) {
        super(name);
        this.size = size;
    }
};


// // 3
// class Labrador extends Dog {
//     constructor(size) {
//         super(name);
//         this.size = size;
//     }
// };


// // 4
// class Labrador extends Dog {
//     constructor(name, size) {
//         this.name = name;
//         this.size = size;
//     }
// };

// 📝 Answer : No.2 will successfully extend the Dog class 



// --------------------------------------------------------
// 🌟 Exercise 6 : Challenges
console.log("*Exercise6*")

// 1. Evaluate these (ie True or False)

// [2] === [2] 
// 📝 false 

// {} === {}
// 📝 SyntaxError: Unexpected token '==='





// 2. What is, for each object below, the value of the property number and why?

const object1 = { number: 5 };
const object2 = object1;
const object3 = object2;
const object4 = { number: 5 };

object1.number = 4;
console.log(object2.number) // 4
console.log(object3.number) // 4
console.log(object4.number) // 5

// 📝 object1,2,3 points at the same adress that stores object1, once number in object1 is modifed to 4, since object 2,3 points at the same obj
// the values of number are also 4. 


// 3. Create a class Animal with the attributes name, type and color. The type is the animal type, for example: dog, cat, dolphin ect …
class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color;
    }
}


class Mamal extends Animal {
    constructor(name, type, color) {
        super(name, type, color)
    }

    sound(animalSound) {
        console.log(`${animalSound} I'am a ${this.type}, named ${this.name} and I'm ${this.color}.`);
    }
}

// it is not specified should color be an array of colors, from description it sounds more like a string
const farmerCow = new Mamal('Lily', 'cow', 'brown and white');
farmerCow.sound("Moos")