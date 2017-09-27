import React, { Component } from 'react';

import {getJson} from '../utils/fetch';
import Auth from "../utils/auth";
import AdminContent from '../components/admin-content';
import SensorsList from '../components/sensors/sensors-list';

class SensorsListPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errorMessage: null,
            sensors: [],
        }
    }

    componentDidMount() {
        this.loadSensors();
    }

    loadSensors() {
        getJson(`/users/${Auth.getUserId()}/sensors`).then(sensors => {
            this.setState({sensors: sensors});
        });
    }

    render() {
        return (
            <AdminContent>
                <SensorsList sensors={this.state.sensors}/>
            </AdminContent>
        )
    }
}

export default SensorsListPage;