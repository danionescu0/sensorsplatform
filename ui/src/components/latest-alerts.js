import React from 'react';
import {
    Table
} from 'ahoy-reactstrap';

const LatestAlerts = ({alerts}) => {
    return (
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