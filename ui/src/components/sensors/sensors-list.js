import React from 'react';
import {Link} from 'react-router-dom';
import {
    Row,
    Col,
    Card,
    CardHeader,
    CardBody,
    CardTitle,
    CardFooter,
    Button,
    Table
} from 'ahoy-reactstrap';

import {SENSOR_TYPES} from './sensors-form';

const SensorsList = ({toogleModal, sensors}) => {
    return (
        <div>
            <Row>
                <Col lg="12">
                    <Card>
                        <CardHeader>
                            <CardTitle>
                                <i className="fa fa-table" aria-hidden="true"/> &nbsp;Sensors list
                            </CardTitle>
                        </CardHeader>
                        <CardBody>
                            <Table hover>
                                <thead>
                                    <tr>
                                        <th>Id</th>
                                        <th>Type</th>
                                        <th>Latest Value</th>
                                        <th>Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {renderRows(sensors)}
                                </tbody>
                            </Table>
                        </CardBody>
                        <CardFooter>
                            <Button color="primary" onClick={toogleModal}>
                                <i className="fa fa-plus" aria-hidden="true"/> &nbsp; Add Sensor
                            </Button>
                        </CardFooter>
                    </Card>
                </Col>
            </Row>
        </div>
    )
};

const renderRows = sensors => {
    return sensors.map((sensor, index) => {
        return (
            <tr key={index}>
                <td>{sensor.id}</td>
                <td>{SENSOR_TYPES[sensor.type]}</td>
                <td>{sensor.latest_value}</td>
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