import React from "react";
import "./index.css";
import {Button, TextField} from "@mui/material";
import * as ReactDOMClient from 'react-dom/client';
import Popup from "./Popup"

class HWSET1 extends React.Component {
  render() {
    return <div> <strong>HWSET1:</strong> {this.props.properties}</div>
  }
}
class HWSET2 extends React.Component {
  render() {
    return <div> <strong>HWSET2:</strong> {this.props.properties}</div>
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
      collaborators: this.props.properties.collaborators.join(', '),
      authUsers: this.props.properties.authorized_users.join(', '),
      authUser:"",
    };
  }
  
  setHw1Check = event =>{
    this.setState({hw1check: event.target.value})
  }

  setHw2Check = event =>{
    this.setState({hw2check: event.target.value})
  }

  setAuthUser = event =>{
    this.setState({authUser: event.target.value})
  }

  render() {
    const handleCheck_in = async() =>{
      try{
        const response = await fetch("http://3.16.154.171:8080/project/" + this.props.properties.project_id + "/checkin", {
          "method": "POST",
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + this.props.token,
          },
          "body": JSON.stringify({
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
          this.props.updateAvail(parseInt(this.props.availhw1) + parseInt(this.state.hw1check), parseInt(this.props.availhw2) + parseInt(this.state.hw2check));
        }

      } catch (err) {
          console.log("Error: " + err)
      }
    }
    
    const handleCheck_out = async() =>{
      try{
        const response = await fetch("http://3.16.154.171:8080/project/" + this.props.properties.project_id + "/checkout", {
          "method": "POST",
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + this.props.token,
          },
          "body": JSON.stringify({
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
          this.props.updateAvail(parseInt(this.props.availhw1) - parseInt(this.state.hw1check), parseInt(this.props.availhw2) - parseInt(this.state.hw2check));
        }

      } catch (err){
          console.log("Error: " + err)
      } 
    }

    const addAuthUser = async() =>{
      console.log(this.state.authUser);
      try{
        const response = await fetch("http://3.16.154.171:8080/project/" + this.props.properties.project_id + "/add_authorized_user", {
          "method": "POST",
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + this.props.token,
          },
          "body": JSON.stringify({
            "user": this.state.authUser,
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
          this.setState({authUsers: result.project_doc.authorized_users.join(', ')});
        }

      } catch (err){
          console.log("Error: " + err)
      } 
    }

    const remAuthUser = async() =>{
      try{
        const response = await fetch("http://3.16.154.171:8080/project/" + this.props.properties.project_id + "/remove_authorized_user", {
          "method": "POST",
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + this.props.token,
          },
          "body": JSON.stringify({
            "user": this.state.authUser,
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
          this.setState({authUsers: result.project_doc.authorized_users.join(', ')});
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
        <div> <strong>AUTHORIZED USERS:</strong> {this.state.authUsers}</div>
        <div> <strong>COLLABORATORS:</strong> {this.state.collaborators}</div>
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
        <div className="auth"><TextField
          hiddenLabel
          id="filled-hidden-label-small"
          variant="filled"
          size="small"
          placeholder="Authorized User"
          onChange={this.setAuthUser}
          value={this.state.authUser}
        />
        <Button variant="contained" className="btn" onClick={addAuthUser}>Add Authorized User</Button>
        <Button variant="contained" className="btn" onClick={remAuthUser}>Remove Authorized User</Button>
        </div>
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
      availhw1:0,
      maxhw1:0,
      availhw2:0,
      maxhw2:0,
      token: " ",
    };

    const login = async() => {
      try{
        let response = await fetch("http://3.16.154.171:8080/login", {
          "method": "POST",
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
          },
          "body": JSON.stringify({"username":"roberto", "password":"roberto"})
        });
          
        if (!response.ok) {
          throw new Error(`Error! status: ${response.status}`);
        }

        let result = await response.json();
        if (result.status === "fail") {
          console.log(result.report);
        } else {
            console.log(result);
            document.cookie = result.access_token
        }
      } catch(err) {
        console.log("Error " + err);
      }
    }

    login();
    let userdoc;

    const get_userdoc = async() => {
      try{
        let response = await fetch("http://3.16.154.171:8080/user/", {
          "method": "POST",
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + document.cookie.split('; ')[1],
          },
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
                "headers": {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer " + document.cookie.split('; ')[1],
                },
              });

              let result = await response.json();
              let project_doc = result.project_doc;
              this.setState({availhw1:result.hardware_doc.availHW1, 
                             availhw2:result.hardware_doc.availHW2,
                             maxhw1:result.hardware_doc.maxHW1,
                             maxhw2:result.hardware_doc.maxHW2})
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
            "Content-Type": "application/json",
            "Authorization": "Bearer " + document.cookie.split('; ')[1],
          },
          "body": JSON.stringify({
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
            "Content-Type": "application/json",
            "Authorization": "Bearer " + document.cookie.split('; ')[1],
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
            "headers": {
              "Accept": "application/json",
              "Content-Type": "application/json",
              "Authorization": "Bearer " + document.cookie.split('; ')[1],
            },
            "body": JSON.stringify({
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
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + document.cookie.split('; ')[1],
          },
          "body":JSON.stringify({"token":"accessToken"})
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

    const updateAvailable = (hw1_available, hw2_available) =>{
      this.setState({availhw1:hw1_available, availhw2:hw2_available});
    }

    const projects = [];
    for (let i = 0; i < this.state.projects_list.length; i++) {
        // note: we are adding a key prop here to allow react to uniquely identify each
        // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
        projects.push(<Project key={i} properties={this.state.projects_list[i]} 
                      updateAvail={updateAvailable} availhw1= {this.state.availhw1} 
                      availhw2= {this.state.availhw2} token={document.cookie.split('; ')[1]}/>);
    }

    return (
      <div>
    
        {this.state.popup && <Popup 
          handleClose= {togglePopup}
          content = {<div>
            {this.state.popmsg}
          </div>}
        />}
        
        <h2>Projects</h2> <Button variant="contained" className="logout" onClick={handleLogout}><strong>Logout</strong></Button>
        <div className="available"><strong>Available HW1: {this.state.availhw1}/{this.state.maxhw1}</strong></div>
        <div className="available"><strong>Available HW2: {this.state.availhw2}/{this.state.maxhw2}</strong></div>
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
        <Button variant="contained" className="btn" onClick={handleAdd}>Create Project</Button>
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
        <Button variant="contained" className="btn" onClick={handleJoin}>Join Project</Button>
        <Button variant="contained" className="btn" onClick={handleLeave}>Leave Project</Button>

        </div>
      </div>
    );
  }
}

// ========================================
const root = ReactDOMClient.createRoot(document.getElementById("root"));
root.render(<Projects />);
