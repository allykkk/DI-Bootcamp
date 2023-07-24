import React from "react";

const QuoteBox = ({ quote, color, onRandom }) => {
  return (
    <div className="quotebox">
      <div className="fadeIn" style={{ color: color }}>
        <h1 id="quote">"{quote.quote}"</h1>
        <h5 id="author">-{quote.author === "" ? "Unknown" : quote.author}-</h5>
      </div>
      <button
        id="newquote"
        style={{ backgroundColor: color }}
        onClick={() => onRandom()}
      >
        New quote
      </button>
    </div>
  );
};

export default QuoteBox;
