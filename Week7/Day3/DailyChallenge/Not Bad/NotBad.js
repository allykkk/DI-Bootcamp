// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.

// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).

// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.

function replaceNotBad(sentence) {
    const wordNot = sentence.indexOf("not");
    const wordBad = sentence.indexOf("bad");

    let newSentence;
    if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
        newSentence = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
    } else {
        newSentence = sentence;
    }
    return newSentence;
}

// Testing function:
const sentence1 = "This dinner is not that bad! You cook well.";
const result1 = replaceNotBad(sentence1);
console.log(result1);

const sentence2 = "This movie is not so bad!";
const result2 = replaceNotBad(sentence2);
console.log(result2);

const sentence3 = "This dinner is bad!";
const result3 = replaceNotBad(sentence3);
console.log(result3);