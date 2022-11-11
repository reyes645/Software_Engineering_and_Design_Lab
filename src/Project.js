import React from "react";
import Popup from "./Popup";
import {Button, TextField} from "@mui/material";
import "./index.css";


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

  export default Project;