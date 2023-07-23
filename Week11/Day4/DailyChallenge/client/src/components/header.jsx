import React, { Component } from "react";

class Header extends Component {
  state = { message: "" };

  async componentDidMount() {
    try {
      const response = await fetch("http://localhost:5000/api/hello");
      const message = await response.text();
      this.setState({ message });
    } catch (error) {
      console.error("Error fetching message:", error);
    }
  }

  render() {
    return <h1>{this.state.message}</h1>;
  }
}

export default Header;
