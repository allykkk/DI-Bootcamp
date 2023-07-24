import React, { Component } from 'react';
import './App.css';
import Header from './components/header';
import Jumbotron from './components/jumbotron';
import HeroCard from './components/heroCard';
import data from "../src/components/data/superheroes.json";
import _ from 'underscore'

class App extends Component {

  state = { heroes: data.superheroes, topScore: 0, game: [] };

  clickHandler = (hero) => {
    let game = [...this.state.game]
    if (this.duplicateHandler(game, hero)) return
    game.push(hero.id)
    let heroes = { ...this.state.heroes }
    heroes = _.shuffle(heroes)
    this.setState({ heroes, game })
  }

  duplicateHandler = (array, currentItem) => {
    const isDuplicate = array.some(item => item === currentItem.id)
    if (isDuplicate) {
      const currentScore = array.length
      if (currentScore > this.state.topScore)
        this.setState({ topScore: currentScore })
      this.setState({ game: [] })
      return true
    }
    return false
  }


  render() {
    return (<div className='wrapper'>
      <header className='container-fluid fixed-top'>
        <Header score={this.state.game.length} topScore={this.state.topScore} />
      </header>
      <div className='jumbotron jumbotron-fluid'>
        <Jumbotron />
      </div>
      <HeroCard heroes={this.state.heroes} clickHandler={this.clickHandler} />
    </div>);
  }
}

export default App;