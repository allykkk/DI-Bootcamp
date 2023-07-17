import React, { Component } from "react";
import ReactDOM from "react-dom";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from "react-responsive-carousel";
import "./style.css";
import { hongkongImage, japanImage, lasvegasImage, macaoImage } from "./assets";

class DemoCarousel extends Component {
  render() {
    return (
      <Carousel>
        <div>
          <img src={hongkongImage} alt="HongKong" />
          <p className="legend">Hong Kong</p>
        </div>
        <div>
          <img src={macaoImage} alt="Macao" />
          <p className="legend">Macao</p>
        </div>
        <div>
          <img src={japanImage} alt="Japan" />
          <p className="legend">Japan</p>
        </div>
        <div>
          <img src={lasvegasImage} alt="LasVegas" />
          <p className="legend">Las Vegas</p>
        </div>
      </Carousel>
    );
  }
}

export default DemoCarousel;

// ReactDOM.render(<DemoCarousel />, document.querySelector('.demo-carousel'));
