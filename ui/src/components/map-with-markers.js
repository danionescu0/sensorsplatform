import React from 'react';
import { compose } from "recompose";
import {
    withScriptjs,
    withGoogleMap,
    GoogleMap,
    Marker
} from "react-google-maps";

const MapWithMarkers = ({markers}) => {
    return (
        <ComposedMapWithMarkers
            googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyBUoFzoykG8NtVh-wezCkZBd5kVF3n_Yiw&libraries=places"
            loadingElement={<div style={{ height: `100%` }} />}
            containerElement={<div style={{ height: `400px` }} />}
            mapElement={<div style={{ height: `100%` }} />}
            markers={markers}
        />
    )
};

export default MapWithMarkers;

const ComposedMapWithMarkers = compose(
    withScriptjs,
    withGoogleMap
)(props =>
    <GoogleMap
        defaultZoom={8}
        defaultCenter={{ lat: 44.40682, lng: 26.2446751 }}
    >
        {renderMarkers(props.markers)}
    </GoogleMap>
);

const renderMarkers = markers => {
    return markers.map((marker, index) => <Marker key={index} {...marker}/>)
};