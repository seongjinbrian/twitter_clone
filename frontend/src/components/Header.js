import React from "react";
import { Navbar, Nav } from "react-bootstrap";
import Cookies from "universal-cookie";

const cookies = new Cookies();
const token = cookies.get("csrf_access_token") || null;
let firstItem = {
  navItem: token ? "Settings" : "Login",
  link: token ? "/settings" : "/login",
};
let secondItem = {
  navItem: token ? "Logout" : "Register",
  link: token ? "/logout" : "/signup",
};
function Header() {
  return (
    <div>
      <Navbar bg="light" expand="lg">
        <Navbar.Brand href="/">Twitter</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto"></Nav>
          <Nav.Link href={firstItem.link} className="mr-sm-2">
            {firstItem.navItem}
          </Nav.Link>
          <Nav.Link href={secondItem.link}>{secondItem.navItem}</Nav.Link>
        </Navbar.Collapse>
      </Navbar>
    </div>
  );
}

export default Header;
