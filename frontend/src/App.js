import "./App.css";
import Home from "./components/Home";
import Header from "./components/Header";
import Login from "./components/Login";
import Signup from "./components/SignUp";
import { BrowserRouter as Router, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Header />
      <Router>
        <Route path="/" exact component={Home} />
        <Route path="/login" exact component={Login} />
        <Route path="/signup" exact component={Signup} />
      </Router>
    </div>
  );
}

export default App;
