import React, { useState } from "react";
import EntryInfo from "./entryInfo";

const Form = () => {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    age: "",
    gender: "",
    destination: "",
    nutsFree: false,
    lactoseFree: false,
    isVegan: false,
  });

  const handleInput = (event) => {
    const { name, value, type, checked } = event.target;
    const newValue = type === "checkbox" ? checked : value;

    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: newValue,
    }));
  };

  const handleSumbit = (event) => {
    event.preventDefault();
    const queryString = new URLSearchParams(formData).toString();
    const port = window.location.port;
    const url = `http://localhost:${port}/?${queryString}`;
    window.location.href = url;
  };

  return (
    <>
      <form className="inputForm" onInput={handleInput}>
        <input
          className="text"
          name="firstName"
          placeholder="First Name"
          value={formData.firstName}
        />
        <br />
        <input
          className="text"
          name="lastName"
          placeholder="Last Name"
          value={formData.lastName}
        />
        <br />
        <input
          className="text"
          name="age"
          placeholder="Age"
          value={formData.age}
        />
        <br />
        <br />

        <label>
          <input
            className="radiobutton"
            type="radio"
            name="gender"
            value="male"
          />
          Male
        </label>
        <label>
          <input
            className="radiobutton"
            type="radio"
            name="gender"
            value="female"
          />
          Female
        </label>
        <br />

        <label className="destination-header">Select your destination</label>
        <br />
        <select className="destination-input" name="destination">
          <option value="">-- Please Choose a destination --</option>
          <option value="Thailand">Thailand</option>
          <option value="Japan">Japan</option>
          <option value="Brazil">Brazil</option>
        </select>
        <br />
        <br />

        <label className="restrictions-title">Dietary restrictions:</label>
        <br />
        <div className="restrictions">
          <input type="checkbox" name="nutsFree" />
          <span>Nuts free</span>
          <br />
          <input type="checkbox" name="lactoseFree" />
          <span>Lactose free</span>
          <br />
          <input type="checkbox" name="isVegan" />
          <span>Vegan</span>
        </div>
        <button className="submit" onSubmit={handleSumbit}>
          Submit
        </button>
      </form>

      <hr />
      <EntryInfo formData={formData} />
    </>
  );
};

export default Form;
