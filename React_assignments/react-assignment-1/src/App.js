import React, { Component } from 'react';
import './App.css';
import UserOutput from './UserOutput/UserOutput';
import UserInput from './UserInput/UserInput';

class App extends Component {

  state = {
    Users : [
      {name : 'Bhanu',
      para1 : "Hello this Bhanu prakash Bikki and this paragragh holds the information that is needed to be displayed in the front end as task1.",
      para2 : "This is the Description the React JS application that is tobe designed and developed by me"},
      {name : 'Bikki',
      para1 : "Hello this  Bikki Follow the instructions explained in the problem video and try to implement a solution on your own. Compare it with my solution (video + downloadable files) thereafter.",
      para2 : "Add styling of your choice to your components/ elements in the components - both with inline styles and stylesheets"}
      ]
  }

  changeUserHandler = (event) => {
    this.setState({
      Users : [
        {name : event.target.value,
        para1 : "Hello this Bhanu prakash Bikki and this paragragh holds the information that is needed to be displayed in the front end as task1.",
        para2 : "This is the Description the React JS application that is tobe designed and developed by me"},
        {name : 'Bikki',
        para1 : "Hello this  Bikki Follow the instructions explained in the problem video and try to implement a solution on your own. Compare it with my solution (video + downloadable files) thereafter.",
        para2 : "Add styling of your choice to your components/ elements in the components - both with inline styles and stylesheets"}
      ]});
  }

  render() {
    return (
      <div clasName = 'App'>
        <UserOutput 
          para1 = {this.state.Users[0].para1} 
          para2 = {this.state.Users[0].para2}
          name = {this.state.Users[0].name}
          values={this.state.Users[0].name}/>
        <UserOutput 
          para1 = {this.state.Users[1].para1} 
          para2 = {this.state.Users[1].para2}
          name = {this.state.Users[1].name}
          values ={this.state.Users[1].name}/>
        <UserInput 
          changes = {this.changeUserHandler}
          currentName = {this.state.Users[0].name}/>
      </div>
    );
  };
}

export default App;
