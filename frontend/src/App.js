import "./App.css";
import Home from "./components/Home";
import Header from "./components/Header";
import Login from "./components/Login";
import Signup from "./components/SignUp";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Check from "./login";
import Main from "./components/Main";
import Logout from "./components/Logout";
import React, { useState } from "react";
import { CookiesProvider } from "react-cookie";
function App() {
  let [login, setLogin] = useState(false);
  // check().then(r => setLogin(r))
  return (
    <CookiesProvider>
      <Header />
      <Router>
        <Route path="/" exact component={Check() ? Main : Home} />
        <Route path="/login" exact component={Login} />
        <Route path="/signup" exact component={Signup} />
        <Route path="/logout" exact component={Logout} />
      </Router>
    </CookiesProvider>
  );
}

export default App;
