import './App.css';
import React, { Component } from 'react';
import QuoteBox from './components/quoteBox';
import quotes from "../src/components/QuotesDatabase";
import _ from 'underscore'


class App extends Component {
  state = { quote: quotes[0], color: this.randomColorGenerator() };

  randomColorGenerator() {
    let randomColor = Math.floor(Math.random() * 16777215).toString(16);
    return `#${randomColor}`
  }

  randomQuoteGenerator = () => {
    const quote = _.sample(quotes);
    const color = this.randomColorGenerator();
    console.log("Entered")
    console.log(quote)
    this.setState({ quote, color })

  }

  render() {
    const { quote, color } = this.state;
    document.body.style.backgroundColor = color;

    return (
      <div style={{ backgroundColor: color }}>
        <QuoteBox quote={quote} onRandom={this.randomQuoteGenerator} color={color} />
      </div>
    );
  }
}

export default App;