import React, { Component } from 'react';
import {withRouter} from 'react-router-dom';

import SensorsForm from '../components/sensors/sensors-form';
import withForm from '../hoc/form';
import {postJson} from "../utils/fetch";
import Auth from "../utils/auth";

class SensorsFormContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errorMessage: null
        }
    }

    handleSubmit(e) {
        const {form} = this.props;
        e.preventDefault();
        if (!form.type) {
            this.setState({
                errorMessage: "Please select sensor type"
            });
            return;
        }
        postJson(`/user-sensors/${Auth.getUserId()}`, form).then(() => {
            this.setState({errorMessage: ""});
            this.props.onAddSuccess();
        }).catch(e => {
            this.setState({errorMessage: "Request failed"});
        });
    }

    render() {
        const {handleInputChange} = this.props;

        return (
            <SensorsForm errorMessage={this.state.errorMessage}
                 handleInputChange={handleInputChange}
                 handleSubmit={this.handleSubmit.bind(this)}
                 toogleModal={this.props.toogleModal}
                 isModalOpen={this.props.isModalOpen}
                 error={this.state.errorMessage}
            />
        )
    }
}

export default withForm(withRouter(SensorsFormContainer));