import React, { Component } from 'react';
import {withRouter} from 'react-router-dom';

import SensorsForm from '../components/sensors/sensors-form';
import withForm from '../hoc/form';
import {postJson} from "../utils/fetch";
import Auth from "../utils/auth";
import AdminContent from '../components/admin-content';

class SensorsFormContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errorMessage: null,
            location: {
                lat: null,
                lng: null,
            },
        }
    }

    onLocationChanged(e) {
        const lat = e.latLng.lat();
        const lng = e.latLng.lng();
        this.setState({
            location: {lat: lat, lng: lng}
        });
    }

    handleSubmit(e) {
        const {form} = this.props;
        e.preventDefault();
        if (!form.type || !form.name) {
            this.setState({
                errorMessage: "Please complete all fields"
            });
            return;
        }
        if (!this.state.location.lng || !this.state.location.lng) {
            this.setState({
                errorMessage: "Please select sensor location on map"
            });
            return;
        }
        const sensor = Object.assign({}, form, this.state.location);
        postJson(`/user-sensors/${Auth.getUserId()}`, sensor).then(() => {
            this.setState({errorMessage: ""});
            this.props.history.push("/sensors");
        }).catch(e => {
            this.setState({errorMessage: "Request failed"});
        });
    }

    render() {
        const {handleInputChange} = this.props;

        return (
            <AdminContent>
                <SensorsForm errorMessage={this.state.errorMessage}
                             handleInputChange={handleInputChange}
                             handleSubmit={this.handleSubmit.bind(this)}
                             error={this.state.errorMessage}
                             onLocationChanged={this.onLocationChanged.bind(this)}
                             location={this.state.location}
                />
            </AdminContent>
        )
    }
}

export default withForm(withRouter(SensorsFormContainer));