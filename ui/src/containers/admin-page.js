import React, { Component } from 'react';

import MapWithMarkers from '../components/map-with-markers';
import LatestAlerts from '../components/latest-alerts'
import {getJson} from '../utils/fetch';
import Auth from "../utils/auth";
import AdminContent from '../components/admin-content';
import ContentBox from '../components/content-box';


class AdminPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errorMessage: null,
            latest_alerts: [],
            sensors: []
        }
    }

    componentDidMount() {
        this.loadLatestAlerts();
        this.loadSensors();
    }

    loadLatestAlerts() {
        getJson(`/alerts/user/${Auth.getUserId()}`).then(latest_alerts => {
            this.setState({latest_alerts: latest_alerts});
        });
    }

    loadSensors() {
        getJson(`/users/${Auth.getUserId()}/sensors`).then(sensors => {
            this.setState({sensors: sensors});
        });
    }

    getSensorsMarkers() {
        return this.state.sensors.map(sensor => ({
            position: { lat: sensor._gis[0], lng: sensor._gis[1] }
        }))
    }

    render() {
        return (
            <AdminContent>
                <ContentBox title="Latest alerts" icon="fa fa-bell" headerClass="bg-danger text-white">
                    <LatestAlerts alerts={this.state.latest_alerts}/>
                </ContentBox>
                <ContentBox title="Sensors positions" icon="fa fa-map-marker" headerClass="bg-info text-white">
                    <MapWithMarkers markers={this.getSensorsMarkers()}/>
                </ContentBox>
            </AdminContent>
        )
    }
}

export default AdminPage;