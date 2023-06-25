// Follow these steps :

// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.

const story = {
    noun: document.querySelector('#noun').value,
    adjective: document.querySelector('#adjective').value,
    person: document.querySelector('#person').value,
    verb: document.querySelector('#verb').value,
    place: document.querySelector('#place').value,
    isEmpty:function(){
        for(let key in story){
            if (!story[key])
                return alert("Please fill in all details!")
            else 
                return true;              
        }
    },
    get madeStory(){
        return`${person} went to ${place} and ${verb} with a ${adjective} ${noun}.`;
    },
}

document.getElementById("libform").addEventListener("submit", (event)=> {
    event.preventDefault(); 
    if (story.isEmpty()) 
    debugger 
        document.getElementById("story").textContent = story.madeStory;
  });



// const noun = document.querySelector('#noun')
// const adjective = document.querySelector('#adjective')
// const person = document.querySelector('#person')
// const verb = document.querySelector('#verb')
// const place = document.querySelector('#place')

