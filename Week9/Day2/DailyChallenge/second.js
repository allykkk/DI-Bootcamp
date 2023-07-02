const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`

const morseObject = JSON.parse(morse);


//   Create three functions. The two first functions should return a promise..

//   The first function is named toJs():
//       this function converts the morse json string provided above to a morse javascript object.
//       if the morse javascript object is empty, throw an error (use reject)
//       else return the morse javascript object (use resolve)
function toJs(jsonStr) {
    return new Promise((resolve, reject) => {
        const morseObject = JSON.parse(morse);
        if (Object.keys(morseObject).length === 0)
            reject(new Error("JS object is empty!"));
        resolve(morseObject);
    })

}

//   The second function called toMorse(morseJS), takes one argument: the new morse javascript object.
//       This function asks the user for a word or a sentence.
//       if the user entered a character that doesn’t exist in the new morse javascript object, throw an error. (use reject)
//       else return an array with the morse translation of the user’s word.

//       if the user enters the word "Hello", the promise resolves with this value ["....", ".", ".-..", ".-..","---"]
//       if the user entered the word "¡Hola!", the promise rejects because the character "¡" doesn't exist in the morse javascript object

function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
        const userInput = prompt("Please type one word: ")
        const array = userInput.toLowerCase().split('');
        const output = []
        array.forEach(element => {
            output.push(morseObject[element])
        });
        const isInvalid = output.some((item) => typeof (item) === 'undefined')
        if (isInvalid)
            reject(new Error('String contains charactor that can not be converted to morse code!'))
        resolve(output);
    })
};


//   The third function called joinWords(morseTranslation), takes one argument: the morse translation array
//       this function joins the morse translation by using line break and display it on the page (ie. On the DOM)

function joinWords(morseTranslation) {
    morseTranslation.forEach(item => console.log(item))
}

//   Chain the three functions.


toJs(morse)
    .then(jsObject => toMorse(jsObject))
    .then(result => joinWords(result))
    .catch(err => console.log(err.message))












