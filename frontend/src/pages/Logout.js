import React, { useEffect } from "react";
import { logout } from "../login";
import { useCookies } from "react-cookie";
import axios from "axios";

function Logout() {
  const [cookies, setCookie, removeCookie] = useCookies([
    "access_token_cookie",
  ]);

  function logout() {
    if (cookies) {
      axios.post("/api/user/logout", {}).then((res) => {
        if (res.data.error) {
          console.error(res.data.error);
        } else {
          window.location = "/";
          return true;
        }
      });
    } else {
      console.log("error");
    }
  }
  useEffect(() => {
    logout();
  });

  return (
    <div className="w3-container w3-xlarge">
      <p>Please wait, logging you out...</p>
    </div>
  );
}

export default Logout;
