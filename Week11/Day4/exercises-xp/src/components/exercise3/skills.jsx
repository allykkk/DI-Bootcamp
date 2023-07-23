import React, { Component } from "react";
import data from "../../data/data.json";

class Skills extends Component {
  state = { Skills: data["Skills"] };
  render() {
    return (
      <ul className="example1 border border-secondary">
        {this.state.Skills.map((item,index) => (
          <div key={index}>
            <h5>{item.Area}</h5>
            <ul>{item.SkillSet.map(skill=><li key={skill.Name}>{skill.Name}</li>)}</ul>
            <br/>
          </div>
        ))}
      </ul>
    );
  }
}

export default Skills;
