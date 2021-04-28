import styled from "styled-components";
import axios from "axios";
import React, {useState} from "react";
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

function Signup() {
  const [signup, setSignup] = useState({"err": ""})
  const register = (e) => {
    e.preventDefault();
    console.log("Hello")
    axios.post("/api/register", {
            email: document.getElementById("email").value,
            username: document.getElementById("username").value,
            password: document.getElementById("password").value,
        })
        .then((res) => {
            console.log(res)
            if (res.data.error) {
                console.log('Hi')
                setSignup({ err: res.data.error });
            } else {
                console.log('hi')
                window.location = "/login"
            }
        });
};
  return (
    <OuterAuth>
      <InnerAuth>
        <form onSubmit={register}>
          <h3>Sign Up</h3>
          <div className="form-group">
            <label>Email address</label>
            <input
              type="email"
              className="form-control"
              placeholder="Type your email"
              id="email"
            />
          </div>

          <div className="form-group">
            <label>Username</label>
            <input
              type="username"
              className="form-control"
              placeholder="Enter Username"
              id="username"
            />
          </div>

          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter Password"
              id="password"
            />
          </div>
          <button type="submit" className="btn btn-primary btn-block">
            Sign Up
          </button>
        </form>
      </InnerAuth>
    </OuterAuth>
  );
}

export default Signup;
