import React from 'react';
import {
    Nav,
    NavItem,
    NavLink,
} from 'ahoy-reactstrap';

const Header = ({logout}) => {
    return (
        <Nav navbar className="ml-auto">
            <NavItem>
                <NavLink href="/" onClick={logout}> <i className="fa fa-fw fa-sign-out"/> Logout </NavLink>
            </NavItem>
        </Nav>
    )
};

export default Header;