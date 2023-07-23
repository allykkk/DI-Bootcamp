import React, { Component } from "react";

class PostForm extends Component {
  state = { message: "" };
  
  submitHandler = async (event) => {
    event.preventDefault();
    const userInput = event.target[0].value;
    const request = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ value: userInput }),
    };
    const url = "http://localhost:5000/api/world";
    try {
      const response = await fetch(url, request);
      const message = await response.text();
      this.setState({ message });
    } catch (error) {
      console.error("Error:", error);
    }
  };

  render() {
    return (
      <form onSubmit={this.submitHandler}>
        <h2>Post to Server:</h2>
        <input name="postMessage" type="text" />
        <button type="submit">Submit</button>
        <p>{this.state.message}</p>
      </form>
    );
  }
}

export default PostForm;
