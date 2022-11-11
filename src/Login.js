import React, { useState } from "react";
import Popup from "./Popup";
import "./App.css";


export const Login = (props) => {
    const [username, setUsername] = useState('');
    const [pass, setPass] = useState('');
    const [popup, setPopup] = useState(false);
    const [popmsg, setMsg] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(username);
    }

    const togglePopup = () => {
        setPopup(!popup)
      } 

    const login = async() => {
        console.log("in login");
        try{
          let response = await fetch("http://3.16.154.171:8080/login", {
            "method": "POST",
            "headers": {
              "Accept": "application/json",
              "Content-Type": "application/json",
            },
            "body": JSON.stringify({"username":username, "password":pass})
          });
          let result = await response.json();
          if (result.status === "fail") {
            console.log(result.report);
            setMsg(result.report)
            console.log(popmsg);
            togglePopup();
          } else {
              console.log(result);
              document.cookie = result.access_token
              props.onFormSwitch('projects')
          }
        } catch(err) {
          console.log("Error " + err);
        }
      }
    return (
        <div className="auth-form-container">
          {popup && <Popup 
            handleClose= {togglePopup}
            content = {<div>
              In popup
              {popmsg}
            </div>}
          />}
            <h2>Login</h2>
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor="username">username</label>
                <input value={username} onChange={(e) => setUsername(e.target.value)}type="username" placeholder="your username" id="username" name="username" />
                <label htmlFor="password">password</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                <button type="submit" onClick={login}>Log In</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('register')}>Don't have an account? Register here.</button>
        </div>
    )
}