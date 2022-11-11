import React, { useState } from "react";
import './App.css';
import { Login } from "./Login";
import { Register } from "./Register";
import Projects from './Projects'

function App() {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }



  return (
    <div className="App">
    {currentForm === 'login' ? (
                <Login onFormSwitch={toggleForm} />
                ) : currentForm === 'register' ? (
                  <Register onFormSwitch={toggleForm} />
                ) : currentForm === 'projects' ? (
                  <Projects onFormSwitch={toggleForm}/>) 
                  : null}
     
    </div>
  );
}

export default App;