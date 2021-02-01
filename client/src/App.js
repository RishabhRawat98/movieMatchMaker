import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import { PrivateRoute, LoggedOutRoute } from "./components";
import { Welcome, Register, Login, MovieList, Swipe } from './pages';
import { Header, Footer } from './layout';
import "bootstrap/dist/css/bootstrap.min.css";
import './App.css';
import jwt_decode from "jwt-decode";
import "regenerator-runtime/runtime";

class App extends Component {

  state = {
    isLoggedIn: false,

    currentUser: {
      id: 0,
      username: " ",
      email: " ",
      password: " ",
    },
  }

  componentDidMount() {
    if (localStorage.getItem("jwtToken")) {
      this.setState({ isLoggedIn: true });
    }
  }

  login = async userData => {
    try {
      const options = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userData),
      };
      const r = await fetch(`http://localhost:3000/users/login`, options);
      const data = await r.json();
      const loginP = document.querySelector("#login");
      loginP.textContent = "";
      if (!data.token) {
        loginP.textContent = data.msg;
        throw Error(data.err);
      }
      const { token } = data;
      console.log(token, "token");
      localStorage.setItem("jwtToken", token);
      const user = jwt_decode(token);
      console.log(user);
      localStorage.setItem("user", user);

      this.setState({ isLoggedIn: true, currentUser: data.user });
      this.props.history.push("/swipe");
    } catch (err) {
      console.warn(`Error: ${err}`);
    }
  };

  render(){
    return(
      <>
        <Header />
        <Switch>
          <LoggedOutRoute exact path="/" isLoggedIn={this.state.isLoggedIn} component={Welcome} />
          <LoggedOutRoute path="/register" isLoggedIn={this.state.isLoggedIn} component={Register} />
          <LoggedOutRoute path="/login" isLoggedIn={this.state.isLoggedIn} login={this.login} component={Login} />
          <PrivateRoute path="/swipe" isLoggedIn={this.state.isLoggedIn} component={Swipe} />
          <PrivateRoute path="/movielist" isLoggedIn={this.state.isLoggedIn} component={MovieList} />
        </Switch>
        <Footer />
      </>
    );
  };

};

export default App;
