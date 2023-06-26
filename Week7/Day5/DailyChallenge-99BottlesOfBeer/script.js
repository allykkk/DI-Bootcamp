const songSection = document.querySelector('#song')


function inputValidation(input) {
    const converted = parseInt(input);
    if (!converted && converted !== 0) {  // in case user input is 0 
        const errorMessage = document.createElement('p')
        errorMessage.textContent = 'Number only!';
        errorMessage.style.color = 'red';
        songSection.appendChild(errorMessage);
    }
    else {
        songSection.innerHTML = '';
    }
    return converted;// if converted is a number - truthy, otherwise return falsy
}

function writeFirstLine(takenNum) {
    const firstLine = document.createElement('p');
    if (takenNum === 1)
        firstLine.textContent = '-> Take _1_ down, pass it around'
    else
        firstLine.textContent = `-> Take _${takenNum}_ down, pass them around`
    songSection.appendChild(firstLine);
}


function writeSecondLine(leftBottle) {
    const secondLine = document.createElement('p');
    if (leftBottle === 0)
        secondLine.textContent = `no bottle of beer on the wall`
    else if (leftBottle === 1)
        secondLine.textContent = `-> we have now 1 bottle`
    else
        secondLine.textContent = `-> we have now ${leftBottle} bottles`
    songSection.appendChild(secondLine);
}



function writeSongBlock(takenNum, LeftNum) {
    writeFirstLine(takenNum);
    writeSecondLine(LeftNum);
    const divider = document.createElement('br');
    songSection.appendChild(divider);
}


addEventListener("submit", (event) => {
    event.preventDefault();
    const bottleNumber = document.getElementById("bottblenum").value;
    const convertedNum = inputValidation(bottleNumber) //inital bottle numbers
    if (convertedNum) { // when input is actual valid number 
        const startLine = document.createElement('p')
        startLine.textContent = `We start the song ${convertedNum} bottles`
        songSection.appendChild(startLine);

        let leftBottle = convertedNum; // inital leftBottle value is the total bottbles amount 

        for (let takenNum = 1; takenNum <= convertedNum; takenNum++) {
            if (leftBottle <= takenNum) {
                takenNum = leftBottle;
                leftBottle = 0;
                writeSongBlock(takenNum, leftBottle);
                break;
            }
            else {
                leftBottle = leftBottle - takenNum;
                writeSongBlock(takenNum, leftBottle);
            };
        }



    }
});