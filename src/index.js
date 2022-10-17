import React from 'react';
import ReactDOM from 'react-dom'
import './index.css';
import {Button, TextField} from '@mui/material';

class HWSET extends React.Component {
  render() {
    return <div>HWSET {this.props.properties.name} {this.props.properties.usage}/{this.props.properties.capacity}</div>
  }
}

class Project extends React.Component {
  render() {
    const handleCheck_in = async() =>{
      try{
        const response = await fetch('http://3.16.154.17:8080/project/{project_id}/checkin', {
          'method': 'POST',
          'body': {
            'token': '',
            'hw1': '',
            'hw2': ''
          },
        });
        
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }

        const result = await response.json();
      } catch {

      } finally {

      }
    }

    const handleCheck_out = async() =>{
      try{
        const response = await fetch('http://3.16.154.17:8080/project/{project_id}/checkout', {
          'method': 'POST',
          'body': {
            'token': '',
            'hw1': '',
            'hw2': ''
          },
        });
        
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }

        const result = await response.json();
      } catch {

      } finally {

      }
    }
    const handleJoin = async() =>{
      try{
        const response = await fetch('http://3.16.154.17:8080/user/join_project', {
          'method': 'POST',
          'body': {
            'token': '',
            'project_id': '',
          },
        });
        
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }

        const result = await response.json();
      } catch {

      } finally {

      }
    }
    return (
      <div>
        <hr />
        <div>NAME:  {this.props.properties.project_name}</div>
        <div>USERS: {this.props.properties.users.toString()}</div>
        <HWSET properties={this.props.properties.hwsets[0]} />
        <TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
        />
        <Button variant="outlined" onClick={handleCheck_in}>Check In</Button>
        <Button variant="outlined" onClick={handleCheck_out}>Check out</Button>
        <HWSET properties={this.props.properties.hwsets[1]} />
        <TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
        />
        <Button variant="outlined">Check In</Button>
        <Button variant="outlined">Check out</Button><br />
        <Button variant="contained" onClick={()=>this.props.clickJoinLeaveButton()}>{this.props.properties.isJoined ? "LEAVE": "JOIN"}</Button>
        <hr />
      </div>
    );
  }
}

class Projects extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      projects: [
        {
          project_name: "Project 1",
          users: ["a", "b"],
          hwsets: [
            {
              name: "1",
              usage: 50,
              capacity: 100,
            },
            {
              name: "2",
              usage: 0,
              capacity: 100,
            }
          ],
          isJoined: false,
        },
        {
          project_name: "Project 2",
          users: ["c", "d"],
          hwsets: [
            {
              name: "1",
              usage: 50,
              capacity: 100,
            },
            {
              name: "2",
              usage: 0,
              capacity: 100,
            }
          ],
          isJoined: true,
        },
        {
          project_name: "Project 3",
          users: ["e", "f"],
          hwsets: [
            {
              name: "1",
              usage: 0,
              capacity: 100,
            },
            {
              name: "2",
              usage: 0,
              capacity: 100,
            }
          ],
          isJoined: false,
        },
      ]
    }
  }
  render() {
    const projects = [];
    for (let i = 0; i < this.state.projects.length; i++) {
        // note: we are adding a key prop here to allow react to uniquely identify each
        // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
        projects.push(<Project key={i} properties={this.state.projects[i]} clickJoinLeaveButton={()=>{var cpy = JSON.parse(JSON.stringify(this.state.projects)); cpy[i].isJoined = !cpy[i].isJoined; console.log(cpy); this.setState({projects: cpy})}} />);
    }
    return (
      <div>
        <p>Projects</p>
        <div>{projects}</div>
      </div>
    );
  }
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Projects />);
