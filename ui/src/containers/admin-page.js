import React, { Component } from 'react';

import MapWithMarkers from '../components/map-with-markers';
import LatestAlerts from '../components/latest-alerts'
import {getJson} from '../utils/fetch';
import Auth from "../utils/auth";
import AdminContent from '../components/admin-content';
import ContentBox from '../components/content-box';


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
                <ContentBox title="Latest alerts" icon="fa fa-bell" headerClass="bg-danger text-white">
                    <LatestAlerts alerts={this.state.latest_alerts}/>
                </ContentBox>
                <ContentBox title="Sensors positions" icon="fa fa-map-marker" headerClass="bg-info text-white">
                    <MapWithMarkers markers={markers}/>
                </ContentBox>
            </AdminContent>
        )
    }
}

export default AdminPage;