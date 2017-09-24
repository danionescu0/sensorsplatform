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
            sensor: [],
        }
    }

    componentDidMount() {
        this.loadSensorData();
    }

    // @ToDo make a request to a new backend get method only for one sensor
    loadSensorData() {
        var sensorId = this.props.match.params.id;
        getJson(`/user-sensors/${Auth.getUserId()}`).then(sensors => {
            for (var sensor in sensors) {
                if (sensorId !== sensors[sensor].id) {
                    continue;
                }
                sensors[sensor].lat = 44.4205602; // fix this
                sensors[sensor].lng = 26.1854989;
                this.setState({sensor: sensors[sensor]});
            }
        });
    }

    render() {
        return (
            <AdminContent>
                <Sensor sensor={this.state.sensor} />
            </AdminContent>
        )
    }
}

export default SensorPage;