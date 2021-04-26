import React from "react";
import { Navbar, Nav } from "react-bootstrap";
// const Nav = styled.div`
//     color: black;
// `;
function Header() {
  return (
    <div>
      <Navbar bg="light" expand="lg">
        <Navbar.Brand href="/">Twitter</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto"></Nav>
          <Nav.Link href="/login" className="mr-sm-2">
            Login
          </Nav.Link>
          <Nav.Link href="/signup">Register</Nav.Link>
        </Navbar.Collapse>
      </Navbar>
    </div>
  );
}

export default Header;
