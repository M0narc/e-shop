import React from 'react'
import { Navbar, Nav, Container } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

function Headers() {
  return (
    <header>
      <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
        <Container>
          {/* redirect to HomePage */}
          <LinkContainer to='/'>
            <Navbar.Brand>E-shop</Navbar.Brand>
          </LinkContainer>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            {/* redirect to cart */}
            <LinkContainer to='/cart'>
              <Nav.Link><i className="fas fa-shopping-cart"></i> Cart</Nav.Link>
            </LinkContainer>
            {/* redirect to login */}
            <LinkContainer to='/login'>
              <Nav.Link><i className="fas fa-user"></i> Login</Nav.Link>
            </LinkContainer>
          </Nav>
        </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  )
}

export default Headers
