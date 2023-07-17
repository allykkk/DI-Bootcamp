import React, { Component } from 'react';
import './Exercise.css'

class Exercise extends Component {
    style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
    };

    render() {
        return (
            <div>
                {/* <h1 style={{ color: "red", backgroundColor: "lightblue" }}>This is a header.</h1> */}
                <h1 style={this.style_header}>This is a header.</h1>
                <p className='para'>This is a paragraph.</p>
                <a href='www.google.com'>This is a link</a>
                <form>
                    <h2>This is a Form:</h2>
                    <p>Enter your name:</p>
                    <input type='text' /><button>Submit</button>
                </form>
                <h3>Here is an image</h3>
                <img src='https://www.freecodecamp.org/news/content/images/2022/04/featured.jpg' />
                <h3>This is  a List</h3>
                <ul>
                    <li>Coffee</li>
                    <li>Tea</li>
                    <li>Milk</li>
                </ul>
            </div>
        );
    }
}

export default Exercise;