import React, { Component } from 'react';

import AdminContent from '../components/admin-content';
import Sensor from '../components/sensors/sensor';

const sensor = {
    id: 1,
    latest_value: 10,
    type: 'temperature',
    lat: 44.4205602,
    lng: 26.1854989,
    latest: [
        {value : 25, timestamp : 1503347176.144763 },
        { value : 25.6, timestamp : 1503347186.294086 },
        { value : 24, timestamp : 1503347196.460394 },
        { value : 26, timestamp : 1503347206.613431 },
        { value : 24, timestamp : 1503347506.613431 },
        { value : 26.1, timestamp : 1503348206.613431 },
        { value : 26.5, timestamp : 1503348406.613431 },
        { value : 26.8, timestamp : 1503348606.613431 },
        { value : 26.3, timestamp : 1503349206.613431 },
    ]
};

class SensorPage extends Component {

    render() {
        return (
            <AdminContent>
                <Sensor sensor={sensor}/>
            </AdminContent>
        )
    }
}

export default SensorPage;