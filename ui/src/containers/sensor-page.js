import React, { Component } from 'react';

import AdminContent from '../components/admin-content';
import Sensor from '../components/sensors/sensor';
import {getJson} from '../utils/fetch';
import Auth from "../utils/auth";

class SensorPage extends Component {
        constructor(props) {
        super(props);
        this.state = {
            errorMessage: null,
            sensor: null,
        }
    }

    componentDidMount() {
        this.loadSensorData();
    }

    // @ToDo make a request to a new backend get method only for one sensor
    loadSensorData() {
        const sensorId = this.props.match.params.id;
        getJson(`/users/${Auth.getUserId()}/sensors`).then(sensors => {
            const sensor = sensors.filter(sensor => sensor.id === sensorId).pop();
            this.setState({sensor: sensor});
        });
    }

    render() {
        return (
            <AdminContent>
                {this.state.sensor && <Sensor sensor={this.state.sensor} />}
            </AdminContent>
        )
    }
}

export default SensorPage;