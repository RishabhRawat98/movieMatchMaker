import React from "react";
import { Switch, Route, Link } from "react-router-dom";
// import { authFetch } from "./auth";
import { Header, Footer } from "./layout";
import { PrivateRoute, LoggedOutRoute } from "./components";
import { Welcome, Register, Login, MovieList, Swipe } from "./pages";
import "bootstrap/dist/css/bootstrap.min.css";

// const PrivateRoute = ({ component: Component, ...rest }) => {
//   const [logged] = useAuth();

//   return (
//     <Route
//       {...rest}
//       render={(props) =>
//         logged ? <Component {...props} /> : <Redirect to="/login" />
//       }
//     />
//   );
// };

class App extends React.Component {
  state = {
    isLoggedIn: false,

    currentUser: {
      id: 0,
      username: " ",
      email: " ",
      password: " ",
    },
  };

  render() {
    return (
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/secret">Secret</Link>
            </li>
          </ul>
        </nav>
        <Header />
        <Switch>
          <LoggedOutRoute exact path="/" component={Welcome} />
          <LoggedOutRoute path="/register" component={Register} />
          <LoggedOutRoute path="/login" component={Login} />
          <Route
            path="/swipe"
            username={this.state.currentUser.username}
            component={Swipe}
          />
          <PrivateRoute
            path="/movielist"
            username={this.state.currentUser.username}
            component={MovieList}
          />
        </Switch>
        <Footer />
      </div>
    );
  }
}

export default App;

function Home() {
  useEffect(() => {
    fetch("/api")
      .then((resp) => resp.json())
      .then((resp) => console.log(resp));
  }, []);
  return <h2>Home</h2>;
}

// function Login(props) {
//   const history = useHistory();
//   const [username, setUsername] = useState("");
//   const [password, setPassword] = useState("");

//   const [logged] = useAuth();

//   const onSubmitClick = (e) => {
//     // e.preventDefault();
//     console.log("You pressed login");
//     let opts = {
//       username: username,
//       password: password,
//     };
//     console.log(opts);
//     fetch("/api/login", {
//       method: "post",
//       body: JSON.stringify(opts),
//     })
//       .then((r) => r.json())
//       .then((token) => {
//         if (token.access_token) {
//           login(token);
//           console.log(token);
//         } else {
//           console.log("Please type in correct username/password");
//         }
//       });
//   };

//   const handleUsernameChange = (e) => {
//     setUsername(e.target.value);
//   };

//   const handlePasswordChange = (e) => {
//     setPassword(e.target.value);
//   };

//   const redirect = (e) => {
//     e.preventDefault();
//     history.push("/register");
//   };

//   return (
//       <div className="container main-form">
//         <div>
//           <p className="form-header"> Enter your details here:</p>
//           <Form action="/secret">
//             <Form.Label>Email:</Form.Label>
//             <Form.Control
//               id="email"
//               type="email"
//               name="email"
//               onChange={handleUsernameChange}
//               value={username}
//               placeholder="Your email"
//             />
//             <br />
//             <Form.Label>Password:</Form.Label>
//             <Form.Control
//               id="password"
//               type="password"
//               name="password"
//               onChange={handlePasswordChange}
//               value={password}
//               placeholder="Your password"
//             />
//             <br />
//             <div className="bottom-form">
//               <Button
//                 variant="info"
//                 type="submit"
//                 onClick={onSubmitClick}
//                 type="submit"
//               >
//                 Log in
//               </Button>
//               <button onClick={() => logout()}>Logout</button>
//               <div className="redirect">
//                 <p>Don't have an account? Sign up here:</p>
//                 <Button
//                   type="submit"
//                   className="main-buttons"
//                   variant="info"
//                   onClick={redirect}
//                 >
//                   Register
//                 </Button>
//               </div>
//             </div>
//           </Form>
//         </div>
//         <p id="login"></p>
//       </div>
//   );
// }

// function Secret() {
//   const [message, setMessage] = useState("");

//   useEffect(() => {
//     authFetch("/api/protected")
//       .then((response) => {
//         if (response.status === 401) {
//           setMessage("Sorry you aren't authorized!");
//           return null;
//         }
//         return response.json();
//       })
//       .then((response) => {
//         if (response && response.message) {
//           setMessage(response.message);
//         }
//       });
//   }, []);

//   return <h2>Secret: test {message}</h2>;
// }
