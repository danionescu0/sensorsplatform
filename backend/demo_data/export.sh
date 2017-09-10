#!/usr/bin/env bash
mongoexport -d multi_sensor_platform -c users --out=users.json
mongoexport -d multi_sensor_platform -c rules --out=rules.json
mongoexport -d multi_sensor_platform -c sensors --out=sensors.json