import React, { Component } from "react";
import Jumbotron from "react-bootstrap/Jumbotron";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { withRouter } from 'react-router-dom';

class Login extends Component {
  state = {
    email: "",
    password: "",
  };

  handleInput = e => this.setState({ [e.target.name]: e.target.value });
  formIncomplete = () => Object.values(this.state).some(v => !v)

  login = e => {
    e.preventDefault();
    this.props.login(this.state);
  };

  redirect = e => {
    e.preventDefault();
    this.props.history.push("/register");
  };

  render() {
    return (
      <Jumbotron>         
          <h1 className="">Welcome back to Movie Matchmaker</h1>
          <div className="formContainer">  
            <p> Enter your details here:</p>
            <Form onSubmit={this.login}>
              <Form.Label>Email:</Form.Label>
              <Form.Control
                id="email"
                type="email"
                name="email"
                value={this.state.email}
                onChange={this.handleInput}
                placeholder="Your email"
              />
              <br />
              <Form.Label>Password:</Form.Label>
              <Form.Control
                id="password"
                type="password"
                name="password"
                value={this.state.password}
                onChange={this.handleInput}
                placeholder="Your password"
              />
              <br />
              <Button className="genButtons" variant="info" type="submit" className={this.formIncomplete() ? 'disabled' : 'enabled'} disabled={this.formIncomplete()}>Log in</Button>
              <label for="quitbtn">Don't have an account? Sign up here:</label>
              <Button id="quitbtn" className="genButtons" variant="info" onClick={this.redirect}>Register</Button>
            </Form>
          </div> 
            <p id="login"></p>  
      </Jumbotron>
    );
  }
}

export default withRouter(Login);