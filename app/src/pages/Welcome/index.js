import React, { Component } from 'react';
import { Link } from "react-router-dom";

class Welcome extends Component {

    render() {
        return (
          <>
            <h1 id="title">Welcome to Movie Matchmaker</h1>
            <div id="welcome-buttons">            
              <button className="main-buttons"><Link to="/register">Register</Link></button>
              <button className="main-buttons"><Link to="/login">Login</Link></button>
            </div>
          </>
        );
    }
}

export default Welcome;