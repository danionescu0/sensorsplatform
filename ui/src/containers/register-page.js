import React, { Component } from 'react';
import {withRouter} from 'react-router-dom';

import Register from '../components/register';
import withForm from '../hoc/form';
import {postJson} from "../utils/fetch";
import {performLogin} from "../utils/login";

class RegisterPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errorMessage: null
        }
    }

    handleSubmit(e) {
        const {form} = this.props;
        e.preventDefault();
        this.validateAndSubmit(form)
    }

    validateAndSubmit(formData) {
        if (formData.password !== formData.confirmed_password) {
            this.setState({errorMessage: 'You write different paswords'});
            return;
        }
        this.performRequest(formData)
    }

    performRequest(formData) {
        postJson('/users',formData).then(() => {
            this.login(formData.email, formData.password);
        }).catch(e => {
            this.setState({errorMessage: "Request failed"});
        });
    }

    login(email, password) {
        const successLoginHandler = () => {
            this.props.history.push('/');
        };
        const failedLoginHandler = () => this.setState({errorMessage: "Failed to login"});
        performLogin(email, password).then(successLoginHandler, failedLoginHandler);
    }

    render() {
        const {handleInputChange} = this.props;

        return (
            <Register errorMessage={this.state.errorMessage}
                   handleInputChange={handleInputChange}
                   handleSubmit={this.handleSubmit.bind(this)}
            />
        )
    }
}

export default withForm(withRouter(RegisterPage));