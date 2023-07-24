import React, { Component } from "react";

const HeroCard = ({ heroes }) => {
  return (
    <>
      {heroes.map((hero) => {
        return (
          <div key={hero.id} className="card">
            <div className="img-container">
              <img src={hero.image} alt={hero.name} />
            </div>
            <div className="img-content">
              <ul>
                <li>
                  <strong>Name: </strong> {hero.name}
                </li>
                <li>
                  <strong>Occupation: </strong> {hero.occupation}
                </li>
              </ul>
            </div>
          </div>
        );
      })}
    </>
  );
};

export default HeroCard;
