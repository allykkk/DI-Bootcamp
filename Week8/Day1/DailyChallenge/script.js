// Follow these steps :

// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.

// Constructor Function 
function Story() {
    this.noun = document.querySelector('#noun').value;
    this.adjective = document.querySelector('#adjective').value;
    this.person = document.querySelector('#person').value;
    this.verb = document.querySelector('#verb').value;
    this.place = document.querySelector('#place').value;
    this.isNotEmpty = function () {
        for (let key in this) {
            if (!this[key]) {
                alert("Please fill in all details!"); // use this instead of console.log
                return false;
            }
        }
        return true;
    };

    this.shuffleStories = function () {
        storiesArray = [
            `In a land filled with ${this.adjective} ${this.noun}s, ${this.person} was known as the bravest of all. Their courage was unmatched, and they fearlessly ${this.verb} through treacherous forests, climbed towering mountains, and crossed vast oceans. One day, they discovered a hidden ${this.place}, rumored to be guarded by mythical creatures. Undeterred, they embarked on a perilous quest to unlock the secrets of the ${this.place}. Their thrilling adventure would be remembered for generations to come.`,
            `Once upon a time, in a wacky world filled with ${this.adjective} ${this.noun}s, ${this.person} had a hilarious mishap. While trying to ${this.verb} at the ${this.place}, they accidentally stumbled and ended up in a comical situation. Laughter echoed through the air as onlookers couldn't help but chuckle at the sight. It became a legendary tale that was shared at parties, making everyone burst into fits of laughter.`,
            `Once upon a time, in a ${this.adjective} land far away, there was a ${this.noun} who longed for love. One day, ${this.person} ${this.verb} into their life and everything changed. Their hearts raced whenever they were together, and they would often meet at the enchanting ${this.place}, where their love blossomed. They lived happily ever after, creating a love story that would be remembered for eternity.`
        ]
        return storiesArray[Math.floor((Math.random() * 3))];
    };

    Object.defineProperty(this, 'madeStory', {
        get: function () {
            return `${this.person} went to ${this.place} and ${this.verb} with a ${this.adjective} ${this.noun}.`;
        }
    });

}

document.getElementById("libform").addEventListener("submit", (event) => {
    event.preventDefault(); //avoid from refreshing 
    const storyInstance = new Story();
    if (storyInstance.isNotEmpty())
        document.getElementById("story").textContent = storyInstance.madeStory;
});


let shuffleCount = 0;
document.getElementById("shuffle-button").addEventListener("click", (event) => {
    event.preventDefault();
    const storyInstance = new Story();
    if (storyInstance.isNotEmpty())
        document.getElementById("story").textContent = storyInstance.shuffleStories();
    shuffleCount++;
    if (shuffleCount > 3) {
        document.getElementById("story").textContent = "You have shuffed too many times";
        document.getElementById("story").style.color = "red"
    };
});
