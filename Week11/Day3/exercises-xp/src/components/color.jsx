import React, { Component } from "react";

class Color extends Component {
  state = { favoriteColor: "red" ,
};

  componentDidMount() {
    console.log("Component mounted");
    setTimeout(() => {
      this.setState({ favoriteColor: "yellow" });
    }, 3000);
  }

  // Part I : shouldComponentUpdate
  shouldComponentUpdate(nextProps, nextState) {
    return true;
  }

  // Part II: componentDidUpdate
  componentDidUpdate(prevProps, prevState) {
    console.log("Component updated");
    console.log("Previous state:", prevState.favoriteColor);
    console.log("Current state:", this.state.favoriteColor);
  }

  // Part III : getSnapshotBeforeUpdate
  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log("In getSnapshotBeforeUpdate");
    return null;
  }

  changeColor = () => {
    this.setState({ favoriteColor: "blue" });
  };

  render() {
    return (
      <div>
        <h2>
          My Favorite Color is <i>{this.state.favoriteColor}</i>
        </h2>
        <button onClick={this.changeColor}>Change Color to Blue</button>
      </div>
    );
  }
}

export default Color;
