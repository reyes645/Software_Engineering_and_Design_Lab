import React from "react";
import "./index.css";
import {Button, TextField} from "@mui/material";
import Popup from "./Popup";
import Project from "./Project";


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

    let userdoc;

    const get_userdoc = async() => {
      console.log(document.cookie.split('; ')[1])
      try{
        let response = await fetch("http://3.16.154.171:8080/user/", {
          "method": "POST",
          "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + document.cookie,
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
                let userdoc = result.user_doc;
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
                let userdoc = result.user_doc;
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
                  let userdoc = result.user_doc;
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
        this.props.onFormSwitch('login');
  
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

export default Projects;

// ========================================

