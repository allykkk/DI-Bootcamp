import React, { Component } from "react";
import data from "../../data/data.json";

class SocialMedias extends Component {
  state = { socialMedias: data['SocialMedias'] };
  render() {
    return (
      <ul className="example1 border border-secondary">
        {this.state.socialMedias.map((item,index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    );
  }
}

export default SocialMedias;
