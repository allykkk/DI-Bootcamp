let client = "John";

const groceries = {
    fruits: ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice: "20$",
    other: {
        payed: true,
        meansOfPayment: ["cash", "creditCard"]
    }
}

// 1. Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method. 
const displayGroceries = () => {
    groceries['fruits'].forEach(fruit => console.log(fruit));
};
displayGroceries();

const cloneGroceries = () => {
    let user = client; // user copied client value -'John'
    client = 'Betty' // client passed new value'Betty'; user -'John'

    let shopping = groceries; // shopping points at groceries;
    groceries['totalPrice'] = "35$";
    groceries['other']['payed'] = false;
    console.log(shopping);
};
cloneGroceries();


// Change the value of the totalPrice key to 35$. Will we also see this modification in the shopping object ? Why ?
// Change the value of the payed key to false. Will we also see this modification in the shopping object ? Why ?
// 📝 Answer : yes, shopping object will also be modified, because both shopping object and groceries objects point at same address
