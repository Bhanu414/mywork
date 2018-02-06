import React, { Component } from 'react';
import './App.css';
import Person from './Person/Person';

class App extends Component {
  state = {
    persons : [
      {name : 'BHanu', age : 25},
      {name: 'Prakash', age : 25},
      {name: 'Bikki', age : 19, hobby: 'PlayStation'},
      {name: 'Bikki', age : 30}

    ],
    other : 'newData'
  }
  switchNameHandler = (newName) => {
    console.log('Was Clicked!')
    // Don't use this method ====>  this.state.persons[0].name = 'Bhanu prakash Bikki'
    this.setState( {
      persons:
      [
        {name : newName, age : 25},
        {name: 'Bobbby', age : 25},
        {name: 'New Bobby', age : 19, hobby: 'xbox'},
        {name: 'New Data', age : 30}
      ]
    } )
  }

  changeHandler = (event) => {
    this.setState( {
      persons:
      [
        {name : event.target.value, age : 25},
        {name: 'prakash', age : 25},
        {name: 'bikki', age : 19, hobby: 'xbox'},
        {name: 'bobby', age : 30}
      ]
    } )
  }



  render() {
    const myStyle = {
      background:'white',
      font:'inherit',
      border:'1px solid blue',
      padding: '8px',
      cursor: 'pointer'
    }
    return (
      <div className="App">
        <h1> Hi, This is React App </h1>
        <button 
          style = {myStyle}
          onClick = {this.switchNameHandler.bind(this,'CHeck')} >Switch</button>
        <Person 
          name = {this.state.persons[0].name} 
          age = {this.state.persons[0].age}
          changes = {this.changeHandler}/>
        <Person 
          name={this.state.persons[1].name} 
          age = {this.state.persons[1].name}
          changes = {this.changeHandler}/>
        <Person 
          name={this.state.persons[2].name} 
          age = {this.state.persons[2].name}
          click = {this.switchNameHandler.bind(this,'Checking')}
          changes = {this.changeHandler}> 
          My Hobby: {this.state.persons[2].hobby}
          
        </Person>
        <Person 
          name={this.state.persons[3].name} 
          age = {this.state.persons[3].name}
          changes = {this.changeHandler}/>  
      </div>
    );

    // return React.createElement('div',{className:'App'},React.createElement('h1',null,'HEllo This is Bhanu\'s site'));
  }
}

export default App;
