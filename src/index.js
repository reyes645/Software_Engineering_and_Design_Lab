import React from "react";
import ReactDOM from "react-dom"
import "./index.css";
import {Button, TextField} from "@mui/material";
import * as ReactDOMClient from 'react-dom/client';

class HWSET1 extends React.Component {
  render() {
    return <div>HWSET {"hw1"} {this.props.properties}/{1000}</div>
  }
}

class HWSET2 extends React.Component {
  render() {
    return <div>HWSET {"hw2"} {this.props.properties}/{1000}</div>
  }
}

class Project extends React.Component {
  render() {
    let hw1 = this.props.properties.hw1;
    let hw2 = this.props.properties.hw2;

    const handleCheck_in = async() =>{
      try{
        const response = await fetch("http://3.16.154.171:8080/project/0/checkin", {
          "method": "POST",
          "body": JSON.stringify({
            "token": "accessToken",
            "hw1": hw1,
            "hw2": hw2
          }),
        });
        
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }
    
        const result = await response.json();

        if (result.status === "fail") {
          console.log(result.report);
        } else{
          hw1 = result.hardwaredoc[0];
          hw2 = result.hardwaredoc[1];
        }

      } catch (err) {
          console.log("Error: " + err)
      } finally {
    
      }
    }
    
    const handleCheck_out = async() =>{
      try{
        const response = await fetch("http://3.16.154.171:8080/project/{project_id}/checkout", {
          "method": "POST",
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          "body": JSON.stringify({
            "token": "user2Token",
            "hw1": hw1,
            "hw2": hw2,
          }),
        });
        
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }
    
        const result = await response.json();

        if (result.status === "fail") {
          console.log(result.report);
        } else{
          hw1 = result.projectdoc.hw1;
          hw2 = result.projectdoc.hw2;
        }

      } catch (err){
          console.log("Error: " + err)
      } finally {
    
      }
    }
    return (
      <div>
        <hr />
        <div>NAME:  {this.props.properties.project_name}</div>
        <div>COLLABORATORS: {this.props.properties.collaborators}</div>
        <HWSET1 properties={hw1} />
        <TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
        />
        <Button variant="outlined" onClick={handleCheck_in}>Check In</Button>
        <Button variant="outlined" onClick={handleCheck_out}>Check out</Button>
        <HWSET2 properties={hw2} />
        <TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
        />
        <Button variant="outlined" onClick={handleCheck_in}>Check In</Button>
        <Button variant="outlined" onClick={handleCheck_in}>Check out</Button><br />
        <Button variant="contained" onClick={()=>this.props.clickJoinLeaveButton()}>{this.props.properties.isJoined ? "LEAVE": "JOIN"}</Button>
        <hr />
      </div>
    );
    
  }
}

class Projects extends React.Component {
  constructor(props) {
    super(props);
    this.state = {projects_list:[]};
    const token = "accessToken"
    let userdoc;
    const get_userdoc = async() => {
      try{
        let response = await fetch("http://3.16.154.171:8080/user/", {
          "method": "POST",
          "mode": "cors",
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json"
          },
          "body": JSON.stringify({"token" : token})
        });
          
      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }

      console.log(response);
      
      let result = await response.json();
      userdoc = result.user_doc;
      console.log("USERDOC", userdoc);

      let projects = [];
      for (let i = 0; i < userdoc.project_list.length; i++) {
        let project_id = userdoc.project_list[i];
        let response = await fetch("http://3.16.154.171:8080/project/" + project_id, {
            "method": "POST",
            "mode": "cors",
            "headers": {
              "Accept": "application/json",
              "Content-Type": "application/json"
            },
              "body": JSON.stringify({"token": token})
            });
            let result = await response.json();
            console.log(result);
            let project_doc = result.project_doc;
            console.log("Project Doc " + i, project_doc);
          projects.push(<Project key={i} properties={project_doc}></Project>)
        }
      } catch(err) {
        console.log("Error " + err);
      } finally {
      
      }
    }
    
    get_userdoc();
  }
  render() {
    const projects = [];
    for (let i = 0; i < this.state.projects_list.length; i++) {
        // note: we are adding a key prop here to allow react to uniquely identify each
        // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
        projects.push(<Project key={i} properties={this.state.projects_list[i]} clickJoinLeaveButton={()=>{var cpy = JSON.parse(JSON.stringify(this.state.projects_list)); cpy[i].isJoined = !cpy[i].isJoined; console.log(cpy); this.setState({projects_list: cpy})}} />);
    }
    return (
      <div>
        <p>Projects <Button variant="contained" className="logout"><strong>Logout</strong></Button></p>
        <div>{projects}</div>
        <div><TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
        />
        <Button variant="contained">Add Project</Button>
        </div>
        <div><TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
        />
        <Button variant="contained">Join Project</Button>

        </div>
      </div>
    );
  }
}


/*const handleJoin = async() =>{
  try{
    const response = await fetch("http://3.16.154.17:8080/user/join_project", {
      "method": "POST",
      headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
      "body": {
        "token": "",
        "project_id": "",
      },
    });
    
    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }

    const result = await response.json();
  } catch (err){
      console.log("Error: " +err);
  } finally {

  }
}
*/
// ========================================
const root = ReactDOMClient.createRoot(document.getElementById("root"));
root.render(<Projects />);
