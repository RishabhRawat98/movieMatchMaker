import React, { useEffect, useState } from "react";
import { login, authFetch, useAuth, logout } from "../../auth";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { withRouter } from "react-router-dom";
import { useHistory } from "react-router";

function Login(props) {
  const history = useHistory();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [logged] = useAuth();

  const onSubmitClick = (e) => {
    // e.preventDefault();
    console.log("You pressed login");
    let opts = {
      username: username,
      password: password,
    };
    console.log(opts);
    fetch("/api/login", {
      method: "post",
      body: JSON.stringify(opts),
    })
      .then((r) => r.json())
      .then((token) => {
        if (token.access_token) {
          login(token);
          console.log(token);
        } else {
          console.log("Please type in correct username/password");
        }
      });
  };

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const redirect = (e) => {
    e.preventDefault();
    history.push("/register");
  };

  return (
    <div className="container main-form">
      <div>
        <p className="form-header"> Enter your details here:</p>
        <Form action="/secret">
          <Form.Label>Email:</Form.Label>
          <Form.Control
            id="email"
            type="email"
            name="email"
            onChange={handleUsernameChange}
            value={username}
            placeholder="Your email"
          />
          <br />
          <Form.Label>Password:</Form.Label>
          <Form.Control
            id="password"
            type="password"
            name="password"
            onChange={handlePasswordChange}
            value={password}
            placeholder="Your password"
          />
          <br />
          <div className="bottom-form">
            <Button
              variant="info"
              type="submit"
              onClick={onSubmitClick}
              type="submit"
            >
              Log in
            </Button>
            <button onClick={() => logout()}>Logout</button>
            <div className="redirect">
              <p>Don't have an account? Sign up here:</p>
              <Button
                type="submit"
                className="main-buttons"
                variant="info"
                onClick={redirect}
              >
                Register
              </Button>
            </div>
          </div>
        </Form>
      </div>
      <p id="login"></p>
    </div>
  );
}

export default withRouter(Login);
