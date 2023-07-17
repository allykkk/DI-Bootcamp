import React, { useState } from 'react';
import Garage from './Garage';



const Car = (props) => {
    const [color, setColor] = useState('blue');

    return (
        <>
            <header>
                This car is {color} {props.model}.
            </header>
            <Garage size="small" />
        </>

    );
}

export default Car;
