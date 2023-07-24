import React from "react";

const Header = ({ score, topScore }) => {
  return (
    <div className="row">
      <h1 className="col-sm-8">Superheroes Memory Game</h1>
      <nav className="col-sm-4">
        <p>
          Score: <span>{score}</span>
        </p>
        <p>
          TopScore: <span>{topScore}</span>
        </p>
      </nav>
    </div>
  );
};

export default Header;
