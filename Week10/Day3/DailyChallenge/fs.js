// Create an fs.js file and use the Node js File System to read the RightLeft file. 
// In the file, you will see a list of symbols : > and <. Each one of this symbol has a meaning:
// > means that you move 1 step to the right
// < means that you move 1 step to the left

// Example:
// When you start reading the file, you start at the position 0
// If the file begins like this ">>>" after 3 steps you would be in position 3
// If the file begins like this ">>><<" after 5 steps you would be in position 1



// Use the corresponding operations to calculate the number of steps needed to hit position the -1 for the first time - The answer should be: 1795 steps.



const fs = require('fs')

fs.readFile('RightLeft.txt', 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
        return
    }
    console.log([...data])
});


// Use the corresponding operations to calculate the final position at the end of the file - The answer should be: 74 steps to the right.
function getPosition() {
    const data = fs.readFileSync('RightLeft.txt', 'utf8')
    left_steps = data.match(/</g).length
    right_steps = data.match(/>/g).length
    steps = right_steps - left_steps
    console.log('Final Position:', steps)
};

getPosition();

// Use the corresponding operations to calculate the number of steps needed to hit position the -1 for the first time - The answer should be: 1795 steps.
function calculateSteps(position) {
    const dataArray = [...fs.readFileSync('RightLeft.txt', 'utf8')]
    let currentPosition = 0
    let stepCount = 0
    for (item of dataArray) {
        stepCount++;
        if (item === '>')
            currentPosition++;
        else currentPosition--;
        if (currentPosition === position) {
            console.log(`Reaching "${position}" for the first time needs ${stepCount} steps`)
            return stepCount
        }
    }
}

calculateSteps(-1);