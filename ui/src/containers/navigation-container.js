import React, {Component} from 'react';
import {withRouter} from 'react-router-dom';

import Navigation from '../components/navigation';
import Auth from "../utils/auth";

class NavigationContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isOpen: false
        };
    }

    toggleNavbar() {
        this.setState({
            isOpen: !this.state.isOpen
        });
    }

    logout(e) {
        e.preventDefault();
        const {history} = this.props;
        Auth.deAuthenticateUser();
        history.push("/login");
    }

    render() {
        return (
            <Navigation isOpen={this.state.isOpen}
                        toogleNavbar={this.toggleNavbar.bind(this)}
                        logout={this.logout.bind(this)}
            />
        )
    }
}

export default withRouter(NavigationContainer);