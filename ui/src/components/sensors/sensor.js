import React from 'react';
import ReactHighcharts from 'react-highcharts';

import MapWithMarkers from '../map-with-markers';
import ContentBox from "../content-box";

const Sensor = ({sensor}) => {
    const marker = {
        position: {lat: sensor._gis[0], lng: sensor._gis[1]},
    };

    return (
        <div>
            <ContentBox title={`Sensor - ${sensor._name}`} icon="fa fa-bar-chart" headerClass="bg-success text-white">
                <ReactHighcharts config={getChartConfig(sensor)}/>
            </ContentBox>
            <ContentBox title={`Sensor ${sensor._name} position`} icon="fa fa-globe" headerClass="bg-danger text-white">
                <MapWithMarkers markers={[marker]}/>
            </ContentBox>
        </div>
    )
};

const getChartConfig = sensor => {
    var chartData = [];
    if (sensor.length !== 0) {
         chartData = sensor.latest.map(value => [value[0] * 1000, parseFloat(value[1])]);
    }

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
            name: sensor.name,
            data: chartData
        }]
    };
};

export default Sensor;