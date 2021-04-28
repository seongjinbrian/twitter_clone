import "./App.css";
import Home from "./components/Home";
import Header from "./components/Header";
import Login from "./components/Login";
import Signup from "./components/SignUp";
import { BrowserRouter as Router, Route } from "react-router-dom";
import {check} from "./login"
import Main from "./components/Main"
import Logout from "./components/Logout"
import React, {useState} from "react";
function App() {
  let [login, setLogin] = useState(false);
  // check().then(r => setLogin(r))
  return (
    <div>
      <Header />
      <Router>
        <Route path="/" exact component = {check() ? Main : Home} />
        <Route path="/login" exact component={Login} />
        <Route path="/signup" exact component={Signup} />
        <Route path="/logout" exact component={Logout} />
      </Router>
    </div>
  );
}

export default App;
