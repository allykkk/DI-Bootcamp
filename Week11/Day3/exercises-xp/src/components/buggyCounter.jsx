import React, { Component } from "react";

class BuggyCounter extends Component {
  state = { counter: 0 };

  handleClick = () => {
    const { counter } = this.state;
    this.setState({ counter: counter + 1 });
  };

  render() {
    if (this.state.counter >= 5) throw new Error("I crashed!");
    return (
      <>
        <h1 onClick={this.handleClick}>{this.state.counter}</h1>
      </>
    );
  }
}

export default BuggyCounter;
