import styled from "styled-components";
import axios from "axios";
import React, {useState, useEffect} from "react";
import {login, check} from "../login"
const OuterAuth = styled.div`
  display: flex;
  justify-content: center;
  flex-direction: column;
  text-align: left;
`;
const InnerAuth = styled.div`
  width: 450px;
  margin: auto;
  margin-top: 25px;
  background: #ffffff;
  box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
  padding: 40px 55px 45px 55px;
  border-radius: 15px;
  transition: all 0.3s;
`;

function Login() {
  // useEffect(() => {
  //   check().then(r => {if (r) {
  //     window.location = "/"
  // }})
  // })
  const [signIn, setSignin] = useState(false);
  const loginEvent = (e) => {
    e.preventDefault();
    login(document.getElementById("email").value, document.getElementById("password").value)
    .then(status => {
      if (status === true) {
        setSignin(true)
        window.location="/"
      } else {
        setSignin(false)
      }
    })
    
  };
  return (
    <OuterAuth>
      <InnerAuth>
        <form onSubmit={loginEvent}>
          <h3>Sign In</h3>
          <div className="form-group">
            <label>Email address</label>
            <input
              type="email"
              className="form-control"
              placeholder="Enter email"
              id="email"
            />
          </div>

          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter password"
              id="password"
            />
          </div>

          <div className="form-group">
            <div className="custom-control custom-checkbox">
              <input
                type="checkbox"
                className="custom-control-input"
                id="customCheck1"
              />
              <label className="custom-control-label" htmlFor="customCheck1">
                Remember me
              </label>
            </div>
          </div>

          <button type="submit" className="btn btn-primary btn-block">
            Submit
          </button>
          <p>
          {signIn && "You're logged in!"}
          </p>
        </form>
      </InnerAuth>
    </OuterAuth>
  );
}

export default Login;
