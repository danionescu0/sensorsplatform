import React from 'react';
import {
    Card,
    CardHeader,
    CardBody,
    Col
} from 'ahoy-reactstrap';

import AdminContent from './admin-content';
import MapWithMarkers from './map-with-markers';

const Admin = () => {

    const markers = [
        {position: { lat: 44.425908, lng: 26.1236888 }},
        {position: { lat: 44.446686, lng: 26.0346153 }},
        {position: { lat: 44.4280871, lng: 26.1271264}},
        {position: { lat: 44.4161778, lng: 26.1509529}},
    ];

    return (
        <AdminContent>
            <Col lg="12">
                <Card className="mb-5">
                    <CardHeader>Sensors positions</CardHeader>
                    <CardBody>
                        <MapWithMarkers markers={markers}/>
                    </CardBody>
                </Card>
            </Col>
        </AdminContent>
    )
};

export default Admin;