import React from 'react';

import {
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Collapse
} from 'ahoy-reactstrap';

import Sidebar from './navigation/sidebar';
import Header from './navigation/header';

const Navigation = ({isOpen, toogleNavbar, logout}) => {
    return (
        <Navbar id="mainNav" className="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
            <NavbarBrand className="navbar-brand-title">Multi Sensors Platform</NavbarBrand>
            <NavbarToggler onClick={toogleNavbar}/>
            <Collapse navbar isOpen={isOpen}>
                <Sidebar/>
                <Header logout={logout}/>
            </Collapse>
        </Navbar>
    )
};

export default Navigation;