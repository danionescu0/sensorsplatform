import React from 'react';
import {
    Input,
    Label,
    FormGroup,
    Button,
    Alert,
} from 'ahoy-reactstrap';

import ContentBox from '../content-box';
import MapWithMarkers from '../map-with-markers';

export const SENSOR_TYPES = {
    temperature: 'Temperature',
    humidity: 'Humidity',
    light: 'Light',
    air_pressure: 'Air pressure',
    gis: 'Gis',
};


const SensorsForm = ({handleInputChange, handleSubmit, error, onLocationChanged, location}) => {
    const marker = {
        position: { lat: location.lat || 44.425908, lng: location.lng || 26.1236888 },
        draggable: true,
        onDragEnd: onLocationChanged
    };

    const footer = <Button color="primary" type="submit" onClick={handleSubmit}>Save</Button>;

    return (
        <ContentBox title="Add Sensor" footer={footer} icon="fa fa-plus" headerClass="bg-success text-white">
            <form onSubmit={handleSubmit} className="mb-5">
                <FormGroup>
                    <Label for="exampleSelect">Name type</Label>
                    <Input required type="text" name="name" placeholder="Write sensor name" onChange={handleInputChange}/>
                </FormGroup>
                <FormGroup>
                    <Label for="exampleSelect">Select sensor type</Label>
                    <Input required type="select" name="type" onChange={handleInputChange}>
                        <option/>
                        {renderOptions()}
                    </Input>
                </FormGroup>
            </form>
            <MapWithMarkers markers={[marker]}/>
            {error && <Alert className="mt-5" color="danger">{error}</Alert>}
        </ContentBox>
    )
};

const renderOptions = () => {
    return Object.keys(SENSOR_TYPES).map(key => <option key={key} value={key}>{SENSOR_TYPES[key]}</option>)
};

export default SensorsForm;