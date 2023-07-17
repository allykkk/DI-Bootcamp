import React, { useState, useEffect } from 'react';

const Color = () => {
    const [favoriteColor, setFavoriteColor] = useState('red')

    useEffect(() => {
        alert('useEffect reached');
        setFavoriteColor('yellow');
    });

    const changeColor = () => {
        setFavoriteColor('blue');
    };

    return (
        <div>
            <h2>My Favourite Color is <i>{favoriteColor}</i></h2>
            <button onClick={changeColor}>Change Color to Blue</button>
        </div>

    );
}

export default Color;