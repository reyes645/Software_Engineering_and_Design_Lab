import React, { useState } from "react";
import ReactDOM from "react-dom"
import "./index.css";
import {Button, TextField} from "@mui/material";
import * as ReactDOMClient from 'react-dom/client';
import Popup from "./Popup"

class HWSET1 extends React.Component {
  render() {
    return <div> <strong>HWSET1:</strong> {this.props.properties}/{1000}</div>
  }
}
class HWSET2 extends React.Component {
  render() {
    return <div> <strong>HWSET2:</strong> {this.props.properties}/{1000}</div>
  }
}
class Project extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hw1: this.props.properties.hw1,
      hw2: this.props.properties.hw2,
      hw1check: 0,
      hw2check: 0,
      popup: false,
      popmsg: "",
    };
  }
  
  setHw1Check = event =>{
    this.setState({hw1check: event.target.value})
  }

  setHw2Check = event =>{
    this.setState({hw2check: event.target.value})
  }

  render() {
    const handleCheck_in = async() =>{
      try{
        console.log("hw1check " + this.state.hw1check)
        const response = await fetch("http://3.16.154.171:8080/project/" + this.props.properties.project_id + "/checkin", {
          "method": "POST",
          "mode": "cors",
          "headers": {
            "Accept": "application/json",
            "Content-Type":"application/json"
          },
          "body": JSON.stringify({
            "token": "accessToken",
            "hw1": parseInt(this.state.hw1check),
            "hw2": parseInt(this.state.hw2check)
          }),
        });
        
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }
    
        const result = await response.json();

        if (result.status === "fail") {
          console.log(result.report);
          this.setState({popmsg: result.report});
          togglePopup();
        } else{
          this.setState({hw1: result.project_doc.hw1});
          console.log("HW1:" + this.state.hw1);
          this.setState({hw2: result.project_doc.hw2});
          console.log("HW2:" + this.state.hw2);

        }

      } catch (err) {
          console.log("Error: " + err)
      }
    }
    
    const handleCheck_out = async() =>{
      try{
        const response = await fetch("http://3.16.154.171:8080/project/" + this.props.properties.project_id + "/checkout", {
          "method": "POST",
          "mode": "cors",
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json"
          },
          "body": JSON.stringify({
            "token": "accessToken",
            "hw1": parseInt(this.state.hw1check),
            "hw2": parseInt(this.state.hw2check)
          }),
        });
        
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }
    
        const result = await response.json();

        if (result.status === "fail") {
          console.log(result.report);
          this.setState({popmsg: result.report});
          togglePopup();
        } else{
          this.setState({hw1: result.project_doc.hw1});
          this.setState({hw2: result.project_doc.hw2});
        }

      } catch (err){
          console.log("Error: " + err)
      } 
    }

    const togglePopup = () => {
      this.setState({popup: !this.state.popup});
    } 

    return (
      <div>
        {this.state.popup && <Popup 
          handleClose= {togglePopup}
          content = {<div>
            {this.state.popmsg}
          </div>}
        />}
        <hr />
        <div> <strong>NAME:</strong> {this.props.properties.project_name}</div>
        <div> <strong>ID:</strong> {this.props.properties.project_id}</div>
        <div> <strong>COLLABORATORS:</strong> {this.props.properties.collaborators.join(', ')}</div>
        <HWSET1 properties={this.state.hw1} />
        <TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
          onChange={this.setHw1Check}
          value={this.state.hw1check}
        />
        <HWSET2 properties={this.state.hw2} />
        <TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
          onChange={this.setHw2Check}
          value={this.state.hw2check}
        />
        <br></br>
        <Button variant="outlined" onClick={handleCheck_in}>Check In</Button>
        <Button variant="outlined" onClick={handleCheck_out}>Check out</Button><br />
        <hr />
      </div>
    );
    
  }
}

class Projects extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      projects_list:[],
      joinID: "",
      addName: "",
      popup: false,
      popmsg: "",
    };
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

        let result = await response.json();
        if (result.status === "fail") {
          console.log(result.report);
        } else {
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
                  "body": JSON.stringify({"token": "accessToken"})
                });
              let result = await response.json();
              let project_doc = result.project_doc;
              console.log("Project Doc " + project_id, project_doc);
              projects.push(project_doc);
            }
            this.setState({projects_list: projects});
        }
      } catch(err) {
        console.log("Error " + err);
      }
    }
    
    get_userdoc();
  }

  setJoinID = event =>{
    this.setState({joinID : event.target.value});
  }

  setAddName = event =>{
    this.setState({addName : event.target.value});
  }

  render() {
    const togglePopup = () => {
      this.setState({popup: !this.state.popup});
    } 

    const handleJoin = async() =>{
      try{
        const response = await fetch("http://3.16.154.171:8080/user/join_project", {
          "method": "POST",
          "headers": {
          "Accept": "application/json",
          "Content-Type": "application/json"
        },
          "body": JSON.stringify({
            "token": "accessToken",
            "project_id": parseInt(this.state.joinID),
          }),
        });
        
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }
        
        let result = await response.json();
        console.log("report: " + result.report);
        this.setState({popmsg: result.report});
        togglePopup();
        if (result.status !== "fail"){
          window.location.reload();
        }
      } catch (err){
          console.log("Error: " +err);
      }
    }

    const handleLeave = async() =>{
      try{
        const response = await fetch("http://3.16.154.171:8080/user/leave_project", {
          "method": "POST",
          "headers": {
          "Accept": "application/json",
          "Content-Type": "application/json"
        },
          "body": JSON.stringify({
            "token": "accessToken",
            "project_id": parseInt(this.state.joinID),
          }),
        });
        
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }
        
        let result = await response.json();
        console.log("status: " + result.report);
        this.setState({popmsg: result.report});
        togglePopup();
        if (result.status !== "fail"){
          window.location.reload();
        }
      } catch (err){
          console.log("Error: " +err);
      }
    }

    const handleAdd = async() =>{
      try{
        console.log(this.state.addName);
        if(this.state.addName !== ""){
          const response = await fetch("http://3.16.154.171:8080/user/add_project", {
            "method": "POST",
            "mode":"cors",
            "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json"
            },
            "body": JSON.stringify({
              "token": "accessToken",
              "project_name": this.state.addName,
            }),
          });
        
          if (!response.ok) {
            throw new Error(`Error! status: ${response.status}`);
          }
          let result = await response.json();
          console.log("report: " + result.report);
          this.setState({popmsg: result.report});
          togglePopup();
          if (result.status !== "fail"){
            window.location.reload();
          }
        }
        
      } catch (err){
          console.log("Error: " + err);
      }
    }

    const handleLogout = async() =>{
      try{
        
        const response = await fetch("http://3.16.154.171:8080/logout", {
          "method": "POST",
          "mode":"cors",
          "headers": {
          "Accept": "application/json",
          "Content-Type": "application/json"
          },
          "body": JSON.stringify({
            "token": "accessToken"
          }),
        });
      
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }
        let result = await response.json();
        console.log("report: " + result.report);
        this.setState({popmsg: result.report});
        togglePopup();
  
      } catch (err){
          console.log("Error: " + err);
      }
    }

    const projects = [];
    for (let i = 0; i < this.state.projects_list.length; i++) {
        // note: we are adding a key prop here to allow react to uniquely identify each
        // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
        projects.push(<Project key={i} properties={this.state.projects_list[i]}  />);
    }

    return (
      <div>
    
        {this.state.popup && <Popup 
          handleClose= {togglePopup}
          content = {<div>
            {this.state.popmsg}
          </div>}
        />}
        
        <p><h2>Projects</h2> <Button variant="contained" className="logout" onClick={handleLogout}><strong>Logout</strong></Button></p>
        <div>{projects}</div>
        <div><TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
          placeholder="Project Name"
          onChange={this.setAddName}
          value={this.state.addName}
        />
        <Button variant="contained" className="addjoin" onClick={handleAdd}>Add Project</Button>
        </div>
        <div><TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
          placeholder="Project ID"
          onChange={this.setJoinID}
          value={this.state.joinID}
        />
        <Button variant="contained" className="addjoin" onClick={handleJoin}>Join Project</Button>
        <Button variant="contained" className="addjoin" onClick={handleLeave}>Leave Project</Button>

        </div>
      </div>
    );
  }
}

// ========================================
const root = ReactDOMClient.createRoot(document.getElementById("root"));
root.render(<Projects />);
