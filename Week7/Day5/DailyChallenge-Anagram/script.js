
function isAnagram(first, second) {
    const firstArray = [...first.replaceAll(' ', '').toLowerCase()].sort()
    const secondArray = [...second.replaceAll(' ', '').toLowerCase()].sort()
    return firstArray.every((letter, index) => {
        return letter === secondArray[index]
    });
}



const program = document.getElementById('program');
const checkResult = document.createElement("p");

addEventListener("submit", (event) => {
    event.preventDefault();
    const firstWord = document.getElementById("first").value;
    const secondWord = document.getElementById("second").value;
    const result = isAnagram(firstWord, secondWord)
    if (result) {
        checkResult.textContent = `✅ "${firstWord}" is an anagram of "${secondWord}" `
    }
    else
        checkResult.textContent = `❌ "${firstWord}" is not an anagram of "${secondWord}" `
    program.appendChild(checkResult)
});

