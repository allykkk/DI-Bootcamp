import React, { Component } from "react";
import data from "../../data/data.json";

class Experiences extends Component {
  state = { Experiences: data["Experiences"] };
  render() {
    return (
      <div className="example1 border border-secondary p-5">
        {this.state.Experiences.map((item,index) => (
          <div className="d-flex flex-column" key={index}>
            <img src={item.logo} alt="logo" width="200" height="200" />
            <p>
              <a href={item.url}>{item.companyName}</a>
            </p>
            <p>
              <b>{item.roles[0].title}</b>
            </p>
            <p>
              {item.roles[0].startDate} {item.roles[0].location}
            </p>
            <p>{item.roles[0].description}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default Experiences;
