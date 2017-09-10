#!/usr/bin/env bash

mongoimport -d multi_sensor_platform -c users --file=users.json
mongoimport -d multi_sensor_platform -c rules --file=rules.json
mongoimport -d multi_sensor_platform -c sensors --file=sensors.json