import React, { Component } from 'react';
import './App.css';
import Header from './components/header';
import Jumbotron from './components/jumbotron';
import HeroCard from './components/heroCard';
import data from "../src/components/data/superheroes.json";


class App extends Component {
  state = { score: 0, topScore: 0, heroes: data.superheroes };

  render() {
    return (<div className='wrapper'>
      <header className='container-fluid fixed-top'>
        <Header score={this.state.score} topScore={this.state.topScore} />
      </header>
      <div className='jumbotron jumbotron-fluid'>
        <Jumbotron />
      </div>
      <HeroCard heroes={this.state.heroes} />
    </div>);
  }
}

export default App;