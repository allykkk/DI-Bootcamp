import React, { useState } from 'react';

const Event = () => {
    const [isToggleOn, setIsToggleOn] = useState(true);

    const clickMe = () => {
        alert('I was clicked');
    };

    const handleKeyDown = (event) => {
        if (event.key=='Enter'){
            alert("The Enter key was pressed, your input is : " + event.target.value)
        }
    }

    const toggleHandler =()=>{
        setIsToggleOn((prevToggle) => !prevToggle);
    }
    
    const style={
        marginTop:'20px'
    }

    return (

        <div>
            <div style={style}><button onClick={clickMe}>Click Me</button></div>
            <div style={style}><input onKeyDown={handleKeyDown} type="text" placeholder="Press the ENTER key!" /></div>
            <div style={{...style,border:"black solid 1px", padding:"15px",width:"9vw",marginLeft: "45%"}} >
                 <p> <b>Exercise 9:</b></p>
                <button onClick={toggleHandler}>
                    {isToggleOn ? 'OFF' :'ON'}
                </button>
             </div>
        </div>
    );
}

export default Event;
