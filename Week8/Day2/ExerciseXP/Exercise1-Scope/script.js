// 🌟 Exercise 1 : Scope

// Analyse the code below, and predict what will be the value of a in all the following functions.
// Write your prediction as comments in a js file. Explain your predictions.


// 1️⃣  #1
function funcOne() {
    const a = 5;
    if (a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}

// #1.1 - run in the console:
funcOne()
// 📝 Answer: a = 3;

// #1.2 What will happen if the variable is declared with const instead of let ?
// 📝 Answer: TypeError: Assignment to constant variable.


// 2️⃣  #2
let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1 - run in the console:
funcThree()
// 📝 Answer: a = 0;
funcTwo()
// 📝 Answer: a = 5;
funcThree()
// 📝 Answer: a = 5;

// #2.2 What will happen if the variable is declared 
// with const instead of let ?
// 📝 Answer: funcTwo() and line 30 funcThree() will not be able to run due to TypeError


// 3️⃣  #3
function funcFour() {
    window.a = "hello";
}


function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console:
funcFour()
// 📝 Answer: a = "hello";
funcFive()
// 📝 Answer: a = "hello";


// 4️⃣  #4
let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}


// #4.1 - run in the console:
funcSix()
// 📝 Answer: a = 1;  inside of funSix() alert result is 'test'


// #4.2 What will happen if the variable is declared 
// with const instead of let ?
// 📝 Answer: does not affect running 



// 5️⃣  #5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console
// 📝 Answer:  Inside a = 5; outside a = 2;

// #5.2 What will happen if the variable is declared 
// with const instead of let ?
// 📝 Answer: does not affect running 