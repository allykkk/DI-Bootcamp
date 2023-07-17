import React, { useState } from 'react';
import './App.css';
import Language from './components/language';

const initialLanguagesState = [
  { name: "Php", votes: 0 },
  { name: "Python", votes: 0 },
  { name: "JavaScript", votes: 0 },
  { name: "Java", votes: 0 }
];

function App() {
  const [languages, setLanguages] = useState(initialLanguagesState);

  const handleClick = (languageName) => {
    setLanguages((prevLanguages) => {
      return prevLanguages.map((language) => {
        if (language.name === languageName)
          return { ...language, votes: language.votes + 1 };
        else return language;
      });
    });
  };

  const handleReset = () => {
    setLanguages(initialLanguagesState);
  }

  return (
    <div>
      <h1>Vote Your Language!</h1>
      <button onClick={handleReset}>Reset</button>
      <div className='languages'>
        {languages.map(item => (
          <Language language={item} key={item.name} handleClick={handleClick} />
        ))}
      </div>
    </div>
  );
}

export default App;
