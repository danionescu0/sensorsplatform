import React from 'react';
import {
    Row,
    Col,
    Card,
    CardHeader,
    CardBody,
    CardTitle,
} from 'ahoy-reactstrap';

const Sensor = ({sensor}) => {
    return (
        <div>
            <Row>
                <Col lg="12">
                    <Card>
                        <CardHeader>
                            <CardTitle>
                                <i className="fa fa-bar-chart" aria-hidden="true"/> &nbsp;Sensor - {sensor.id}
                            </CardTitle>
                        </CardHeader>
                        <CardBody>
                        </CardBody>
                    </Card>
                </Col>
            </Row>
        </div>
    )
};

export default Sensor;