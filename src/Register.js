import React, { useState } from "react";
import Popup from './Popup'

export const Register = (props) => {
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

    const signup = async() => {
        console.log("in login");
        try{
          let response = await fetch("http://3.16.154.171:8080/signup", {
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
              props.onFormSwitch('login')
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
            <h2>Register</h2>
        <form className="register-form" onSubmit={handleSubmit}>
            <label htmlFor="username">username</label>
            <input value={username} onChange={(e) => setUsername(e.target.value)}type="username" placeholder="your username" id="username" name="username" />
            <label htmlFor="password">password</label>
            <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
            <button type="submit" onClick={signup}>Register</button>
        </form>
        <button className="link-btn" onClick={() => props.onFormSwitch('login')}>Already have an account? Login here.</button>
    </div>
    )
}