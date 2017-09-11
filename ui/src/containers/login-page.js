import React, { Component } from 'react';
import {withRouter} from 'react-router-dom';

import Login from '../components/login';
import withForm from '../hoc/form';
import {performLogin} from "../utils/login";

class LoginPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            failedLogin: false
        }
    }

    handleSubmit(e) {
        const {form, history} = this.props;
        const successLoginHandler = () => {
            history.push('/');
            this.setState({failedLogin: true})
        };
        const failedLoginHandler = () => this.setState({failedLogin: true});

        performLogin(form.email, form.password).then(successLoginHandler.bind(this), failedLoginHandler.bind(this));
        e.preventDefault();
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