import logo from './logo.svg';
import './App.css';
import UserFavoriteAnimals from './Day1/UserFavoriteAnimals';
import Exercise from './Day1/Exercise3';


// Exercise 1: with JSX
// Instructions

//     In the App.js file, display a “Hello World!” message in a paragraph.
//     Create a constant variable with JSX const myelement = <h1>I Love JSX!</h1>;, and render it on the page.
//     Create a constant variable named sum, which value is 5 + 5. Render on the page, the following sentence "React is <sum> times better with JSX"

const myelement = <h1>I Love JSX!</h1>;

const sum = 5 + 5;

const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals: ['Horse', 'Turtle', 'Elephant', 'Monkey']
};


function App() {
  return (
    <div className="App">
      <p>Hello World!</p>
      {myelement}
      <p>React is {sum} times better with JSX</p>
      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      <UserFavoriteAnimals favAnimals={user.favAnimals} />
      <Exercise />
    </div>

  );
}

export default App;
