const largeNumber = 356;


function currentTime() {
    const currentDate = new Date();
    return currentDate.toString();
}

// console.log(currentTime())


module.exports = {
    largeNumber: largeNumber,
    currentTime: currentTime
};