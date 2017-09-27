import React from 'react';
import {Link} from 'react-router-dom';
import {
    Button,
    Table
} from 'ahoy-reactstrap';
import ContentBox from '../content-box';

import {SENSOR_TYPES} from './sensors-form';

const SensorsList = ({sensors}) => {
    return (
        <ContentBox title="Sensors list" footer={getFooter()} icon="fa fa-table" headerClass="bg-success text-white">
            <Table hover>
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Latest Value</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                {renderRows(sensors)}
                </tbody>
            </Table>
        </ContentBox>

    )
};

const getFooter = () => {
    return (
        <Link to="/sensors/add" >
            <Button color="success">
                <i className="fa fa-plus" aria-hidden="true"/> &nbsp; Add Sensor
            </Button>
        </Link>
    )
};

const renderRows = sensors => {
    return sensors.map((sensor, index) => {
        return (
            <tr key={index}>
                <td>{sensor.id}</td>
                <td>{sensor._name}</td>
                <td>{SENSOR_TYPES[sensor.type]}</td>
                <td>
                    {sensor.latest_value.hasOwnProperty('lat')  ?
                        sensor.latest_value.lat + ' & ' + sensor.latest_value.lng : sensor.latest_value}
                </td>

                <td>
                    <Link to={`/sensors/${sensor.id}`}>
                        <Button color="primary"><i className="fa fa-info-circle"/> {' '}Details</Button>
                    </Link>
                </td>
            </tr>
        )
    });
};

export default SensorsList;