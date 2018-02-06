import React from 'react';
import './UserOutput.css';

const UserOutput = (props) => {
    return(
    <div className = 'User'>
        <h1> User : {props.name}</h1>
        <table id = 'table'>
            <tr> 
                <th>Name</th>
                <th>First Para</th>
                <th>Second Para</th>
            </tr>
            <tr>
                <td>{props.values}</td>
                <td>{props.para1} </td>
                <td>{props.para2} </td>
            </tr>
        </table>
    </div>
    );

};

export default UserOutput;