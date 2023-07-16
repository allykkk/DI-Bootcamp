// Exercise 2 : Object
// Instructions

// Using the following object:

// const user = {
//   firstName: 'Bob',
//   lastName: 'Dylan',
//   favAnimals : ['Horse','Turtle','Elephant','Monkey']
// };

//     In the App.js file, render the first name and the last name of the user in two <h3>.
//     In a separate Javascript file named UserFavoriteAnimals.js, create a new Class Component called UserFavoriteAnimals. Use props to pass the favAnimals array to the UserFavoriteColors component.
//     In the UserFavoriteColors component, use the map method to create <li> tags in a <ul> tag.
//         Each <li> corresponds to one animal from the favAnimals array.
//         Display the <li> tags. Tip : You can use the second parameter of the map function as a key to uniquely identify each HTML item
import React, { Component } from 'react';


class UserFavoriteAnimals extends Component {
    render() {
        const favAnimals = ['Horse', 'Turtle', 'Elephant', 'Monkey'];
        return (
            <ul>
                {favAnimals.map((animal, index) => {
                    return <li key={index}>{animal}</li>
                })}
            </ul>
        );
    }
}

export default UserFavoriteAnimals;
