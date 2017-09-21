import React from 'react';
import ReactHighcharts from 'react-highcharts';
import { compose } from "recompose";
import {
    withScriptjs,
    withGoogleMap,
    GoogleMap,
    Marker,
} from "react-google-maps";

import SensorBox from "./sensor-box";

const Sensor = ({sensor}) => {

    return (
        <div>
            <SensorBox title={`Sensor - ${sensor.id}`} icon="fa fa-bar-chart">
                <ReactHighcharts config={getChartConfig(sensor)}/>
            </SensorBox>
            <SensorBox title={`Sensor ${sensor.id} position`} icon="fa fa-globe">
                <SensorMap
                    googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyBUoFzoykG8NtVh-wezCkZBd5kVF3n_Yiw&libraries=places"
                    loadingElement={<div style={{ height: `100%` }} />}
                    containerElement={<div style={{ height: `400px` }} />}
                    mapElement={<div style={{ height: `100%` }}/>}
                    markerPosition={{lat: sensor.lat, lng: sensor.lng}}
                />
            </SensorBox>
        </div>
    )
};


const SensorMap = compose(
    withScriptjs,
    withGoogleMap
)(props =>
    <GoogleMap
        defaultZoom={8}
        defaultCenter={{ lat: 44.40682, lng: 26.2446751 }}
    >
        <Marker
            position={props.markerPosition}
        />
    </GoogleMap>
);

const getChartConfig = sensor => {
    const chartData = sensor.latest.map(value => [value.timestamp * 1000, value.value]);

    return {
        chart: {
            zoomType: 'x',
            type: 'spline'
        },
        title: {
            text: `Latest values for sensor with id ${sensor.id}`
        },
        xAxis: {
            type: 'datetime'
        },
        plotOptions: {
            spline: {
                marker: {
                    enabled: true
                }
            }
        },
        series: [{
            name: sensor.id,
            data: chartData
        }]
    };
};

export default Sensor;