import Axios from "axios";
import { useCookies } from "react-cookie";
import React, { useState, useEffect } from "react";
import Cookies from "universal-cookie";

const Check = () => {
  const cookies = new Cookies();
  const myCookie = cookies.get("csrf_access_token") || null; // Pacman
  let isCookie = true;
  if (myCookie == null) {
    isCookie = false;
  }
  return isCookie;
};

export default Check;
