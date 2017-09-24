import React from 'react';
import { compose } from "recompose";
import {
    Row,
    Col,
    Card,
    CardHeader,
    CardBody,
    CardTitle,
    Table
} from 'ahoy-reactstrap';

const LatestAlerts = ({alerts}) => {
    return (
        <div>
            <Row>
                <Col lg="12">
                    <Card>
                        <CardHeader>
                            <CardTitle>
                                <i className="fa fa-table" aria-hidden="true"/> &nbsp;Latest alerts
                            </CardTitle>
                        </CardHeader>
                        <CardBody>
                            <Table hover>
                                <thead>
                                    <tr>
                                        <th>Date</th>
                                        <th>Rule name</th>
                                        <th>Rule conditions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {renderRows(alerts)}
                                </tbody>
                            </Table>
                        </CardBody>
                    </Card>
                </Col>
            </Row>
        </div>
    )
};

const renderRows = alerts => {
    return alerts.map((alert, index) => {
        return (
            <tr key={index}>
                <td>{alert.date}</td>
                <td>{alert.name}</td>
                <td>{alert.rule_text}</td>
            </tr>
        )
    });
};

export default LatestAlerts;