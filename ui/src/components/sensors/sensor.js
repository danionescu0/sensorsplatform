import React from 'react';
import ReactHighcharts from 'react-highcharts';

import MapWithMarkers from '../map-with-markers';
import SensorBox from "./sensor-box";

const Sensor = ({sensor}) => {
    const marker = {
        position: {lat: sensor.lat, lng: sensor.lng},
    };

    return (
        <div>
            <SensorBox title={`Sensor - ${sensor.id}`} icon="fa fa-bar-chart">
                <ReactHighcharts config={getChartConfig(sensor)}/>
            </SensorBox>
            <SensorBox title={`Sensor ${sensor.id} position`} icon="fa fa-globe">
                <MapWithMarkers markers={[marker]}/>
            </SensorBox>
        </div>
    )
};

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