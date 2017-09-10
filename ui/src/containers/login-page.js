import React, { Component } from 'react';
import {withRouter} from 'react-router-dom';

import Login from '../components/login';
import withForm from '../hoc/form';
import {doFetch} from "../utils/fetch";
import Auth from "../utils/auth";

class LoginPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            failedLogin: false
        }
    }

    handleSubmit(e) {
        const {form} = this.props;
        const params = new URLSearchParams();
        params.set("email", form.email);
        params.set("password", form.password);
        this.doLogin(params);
        e.preventDefault();
    }

    doLogin(params) {
        const {history} = this.props;

        doFetch('/auth', {
            body: params,
            method: 'POST'
        }).then(response => response.text())
        .then(token => {
            this.setState({failedLogin: false});
            Auth.authenticateUser(token);
            history.push('/');
        }).catch(e => {
            console.log(e);
            this.setState({failedLogin: true});
        });
    }

    render() {
        const {handleInputChange} = this.props;

        return (
            <Login failedLogin={this.state.failedLogin}
                   handleInputChange={handleInputChange}
                   handleSubmit={this.handleSubmit.bind(this)}
            />
        )
    }
}

export default withForm(withRouter(LoginPage));