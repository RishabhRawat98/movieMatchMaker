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
      <div className="container main-form">
          <div>  
            <p className="form-header"> Enter your details here:</p>
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
              <div className="bottom-form">
                <Button variant="info" type="submit" className={this.formIncomplete() ? 'disabled' : 'enabled', 'main-buttons'} disabled={this.formIncomplete()}>Log in</Button>
                <div className="redirect">
                  <p>Don't have an account? Sign up here:</p>
                  <Button className="main-buttons" variant="info" onClick={this.redirect}>Register</Button>
                </div>
              </div>
            </Form>
          </div> 
            <p id="login"></p>  
      </div>
    );
  }
}

export default withRouter(Login);