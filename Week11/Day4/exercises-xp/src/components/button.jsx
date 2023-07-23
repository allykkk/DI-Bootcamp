import React from "react";
import axios from "axios";

const Button = () => {
  const url = "https://webhook.site/34e20c00-9c6d-4576-baa8-eeddc1959c5e";
  const data = {
    key1: "myusername",
    email: "mymail@gmail.com",
    name: "Isaac",
    lastname: "Doe",
    age: 27,
  };

  const clickHandler = async () => {
    try {
      const response = await axios.post(url, JSON.stringify(data), {
        "Content-Type": "application/json",
      });
      console.log(response);
    } catch (error) {
      console.error(`Error: ${error.message}`);
    }
  };

  return (
    <>
      <button onClick={clickHandler}>Press me to post some data</button>
    </>
  );
};

export default Button;
