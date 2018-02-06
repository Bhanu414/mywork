import React from 'react';
import './UserInput.css';

const UserInput = (props) => {
    return (
        <div className='User'>
            <input type = 'text' onChange = {props.changes}
            value = {props.currentName}/>
            {/* <button id = 'button' >SUBMIT</button> */}
        </div>
    );
};

export default UserInput;