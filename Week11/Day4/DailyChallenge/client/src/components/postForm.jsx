import React, { Component } from "react";

class PostForm extends Component {
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
      console.log(await response.text());
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
      </form>
    );
  }
}

export default PostForm;
