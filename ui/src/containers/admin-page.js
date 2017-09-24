import React, { Component } from 'react';
import {
    Card,
    CardHeader,
    CardBody,
    Col
} from 'ahoy-reactstrap';

import MapWithMarkers from '../components/map-with-markers';
import LatestAlerts from '../components/latest-alerts'
import {getJson} from '../utils/fetch';
import Auth from "../utils/auth";
import AdminContent from '../components/admin-content';

const markers = [
    {position: { lat: 44.425908, lng: 26.1236888 }},
    {position: { lat: 44.446686, lng: 26.0346153 }},
    {position: { lat: 44.4280871, lng: 26.1271264}},
    {position: { lat: 44.4161778, lng: 26.1509529}},
];

class AdminPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errorMessage: null,
            latest_alerts: [],
        }
    }

    componentDidMount() {
        this.loadLatestAlerts();
    }

    loadLatestAlerts() {
        getJson(`/alerts/user/${Auth.getUserId()}`).then(latest_alerts => {
            this.setState({latest_alerts: latest_alerts});
        });
    }

    render() {
        return (
            <AdminContent>
                <Col lg="12">
                    <Card className="mb-5">
                        <CardHeader>Sensors positions</CardHeader>
                        <CardBody>
                            <LatestAlerts alerts={this.state.latest_alerts}/>
                            <MapWithMarkers markers={markers}/>
                        </CardBody>
                    </Card>
                </Col>
            </AdminContent>
        )
    }
}

export default AdminPage;