import React from 'react';
import './Person.css';

const person = (props) => {
   return (
        <div className ='Person' >
            <p onClick = {props.click}> I'm {props.name} having age {props.age} and this page with id of {Math.floor(Math.random()*50000)}</p>
            <p> {props.children} </p>
            <input type='text' onChange = {props.changes} />
        </div>

   )
};
export default person;