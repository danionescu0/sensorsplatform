import React, { Component } from 'react';

import {getJson} from '../utils/fetch';
import Auth from "../utils/auth";
import AdminContent from '../components/admin-content';
import SensorsList from '../components/sensors/sensors-list';
import SensorsFormContainer from './sensors-form-container';

class SensorsListPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errorMessage: null,
            sensors: [],
            isModalOpen: false
        }
    }

    toogleModal() {
        this.setState({
            isModalOpen: !this.state.isModalOpen
        });
    }

    componentDidMount() {
        this.loadSensors();
    }

    loadSensors() {
        getJson(`/user-sensors/${Auth.getUserId()}`).then(sensors => {
            this.setState({sensors: sensors});
        });
    }

    onAddSuccess() {
        this.setState({
            isModalOpen: false
        });
    }

    render() {
        return (
            <AdminContent>
                <SensorsFormContainer
                    toogleModal={this.toogleModal.bind(this)}
                    isModalOpen={this.state.isModalOpen}
                    onAddSuccess={this.onAddSuccess.bind(this)}
                />
                <SensorsList toogleModal={this.toogleModal.bind(this)} sensors={this.state.sensors}/>
            </AdminContent>
        )
    }
}

export default SensorsListPage;