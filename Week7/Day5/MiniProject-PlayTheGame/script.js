function inputValidation() {
    const userInput = prompt("Enter a number between 0 and 10:");
    const converted = parseInt(userInput);
    if (!converted && converted !== 0) // in case user input is 0 
        alert("Sorry Not a number, Goodbye");
    if (converted > 10 || converted < 0) {
        alert("Sorry it’s not a good number, Goodbye")
        return false
    }
    // if converted is a number that between 0-10  - truthy, otherwise return falsy
    return converted
}


function compareNumbers(userNumber, computerNumber) {
    if (userNumber === computerNumber) {
        alert("“WINNER”");
        return true
    }
    if (userNumber > computerNumber)
        alert(`Your number is bigger then the computer’s, guess again`);
    if (userNumber < computerNumber)
        alert(`Your number is smaller then the computer’s, guess again`)
    return false
}


function playTheGame() {
    const willPlay = confirm("Would you like to play the game?");
    if (!willPlay)
        alert("No problem, Goodbye");
    else {
        let isBreak = false;
        let userNumber = inputValidation(); // get cleaned userInput from this function'
        // userInput is invalid - break 
        if (!userNumber && userNumber !== 0) // in case user input is 0 
            isBreak = true;
        else { // userInput is valid - continute
            const computerNumber = Math.floor(Math.random() * 11);
            let count = 0; // add counter for bigger than 3 comparision 
            while (!isBreak) {
                const result = compareNumbers(userNumber, computerNumber) // true - winner / false - different value
                if (result) // when result is true - winner 
                    isBreak = true;
                else { // result is false - do it again 
                    count++;
                    if (count >= 3) { // when played 3 times, break
                        isBreak = true;
                        alert("out of chances");
                    }
                    else { // else continue 
                        userNumber = inputValidation();
                    }
                };
            };
        };



    }
}