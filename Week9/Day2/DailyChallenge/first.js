// 1rst daily challenge

//     Create two functions. Each function should return a promise.
//     The first function called makeAllCaps(), takes an array of words as an argument
//         If all the words in the array are strings, resolve the promise. The value of the resolved promise is the array of words uppercased.
//         else, reject the promise with a reason.
//     The second function called sortWords(), takes an array of words uppercased as an argument
//         If the array length is bigger than 4, resolve the promise. The value of the resolved promise is the array of words sorted in alphabetical order.
//         else, reject the promise with a reason.


//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log('First: ', result))
    .catch(error => console.log('First: ', error.message))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log('Second: ', result))
    .catch(error => console.log('Second: ', error.message))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log('Thrid: ', result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
    .catch(error => console.log('Thrid: ', error.message))


function makeAllCaps(array) {
    return new Promise((resolve, reject) => {
        const isAllString = array.every(item => typeof (item) === 'string');
        if (isAllString)
            resolve(array.map((item) => item.toUpperCase()));
        else
            reject(new Error('Not all items in the arrat are strings!'))
    })
}

function sortWords(array) {
    return new Promise((resolve, reject) => {
        if (array.length > 4)
            resolve(array.sort());
        else
            reject(new Error('Array length is smaller or equal to 4'))
    })
}


