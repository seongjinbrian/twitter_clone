import Axios from "axios";
import { useCookies } from "react-cookie";
import React, { useState, useEffect } from "react";

const Check = () => {
  const [cookies, setCookie, removeCookie] = useCookies([
    "access_token_cookie",
  ]);
  console.log(cookies);
  if (cookies) {
    return true;
  } else {
    return false;
  }
};
// function check() {
//   const [cookies, setCookie, removeCookie] = useCookies([
//     "access_token_cookie",
//   ]);
// }

export default Check;
