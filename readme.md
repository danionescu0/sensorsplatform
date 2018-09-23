# Motivation
In the IOT era being connected and informed all the time is the thing that matters. 

This platform enables you to make rapid decisions and possibly prevent human or property loss.


My vision implies that we connect existing resources (sensors, data sources) and manage them without any programming knowledge  in a simple web interface.

For example using data from gps devices from a fleet of cars minimal or maximal distances car alerts can be emited 
or maybe maximum speed limits exceded alerts.

So what should the platform do, to enable these things:

* Have a friendly web interface to enable non programmers to use it
* Make rapid decisions from the data of multiple sensors
* Support a large number of sensor data
* Instant alerts (SMS, Email, Push etc)
* Big Data analysis 
* Integrate actuator platforms like IFTTT to control the psichical world

# Diagrams

## Platform overview
![platform_overview.png](https://github.com/danionescu0/sensorsplatform/blob/master/media/platform_overview.png)

## Sensors deployment
![sensor_deployment.png](https://github.com/danionescu0/sensorsplatform/blob/master/media/sensor_deployment.png)

## Internal structure
![internal_structure.png](https://github.com/danionescu0/sensorsplatform/blob/master/media/internal_structure.png)

# Screenshots

## Add rule
![multisensorplatform-add-rule.jpg](https://github.com/danionescu0/sensorsplatform/blob/master/media/multisensorplatform-add-rule.jpg)

## Dashboard
![multisensorplatform-dashboard.png](https://github.com/danionescu0/sensorsplatform/blob/master/media/multisensorplatform-dashboard.png)

## Sensor page
![multisensorplatform-sensor-page.jpg](https://github.com/danionescu0/sensorsplatform/blob/master/media/multisensorplatform-sensor-page.jpg)


# Posible usecases

1. Basement / warehouses monitoring

- Sensors: humidity, flood, gases, presence, noise

- Purpose: detect intrusion, flood, toxic gases, water infiltration

- Actions taken: alert, enable ventilation, close gas and water supply

- Powering: wall power supply, batteries, TEG generator

2. VoIP integration usecases:

- SMS alerts
- VOICE alerts
- Calls a list of numbers until ACK given
- Call a number and get the latest alerts (via voice or sms)
- ACTIVATE IFTTT rules using voice or SMS

3. Car fleet monitoring
- Sensors: gps, temperature
- Purpose: speed limit exceded, min distance not achieved, max distance exceded, temperature not in range (for trucks with special loads). The GPS monitoring can be implemented using a phone application
- Actions taken: alert
- Powering: car power supply

4. Agriculture monitoring

- Sensors: air temperature humidity, soil humidity, PH meter, wind speed, UV, solar light spectrum
- Purpose: detect hazards, enable prevention measurements, predict problems and prevent them before happen with ML
- Actions taken: alert, irrigation, nutrients distribution
- Powering:  batteries, solar power

5. City environmental monitoring

- Sensors: humidity, temperature, UV, wind speed, particle, gas, radiation
- Purpose: detect hazards, warn the population to stay in doors, wear protective clothing, masks
- Actions taken: alerts, recommendations: mask, suncreme, protective clothing, using a mobile app warn for too much sun exposure, expose the information in a website to raise public awareness
- Powering: wall power supply, batteries, solar

6. Smart parking

- Sensors: parking magnetical sensor / visual image processing
- Purpose: detect free parking spots
- Actions taken: design an app / integrate with navigation apps to find free parking spots
- Powering: batteries, solar, power plug

7. Water hazard monitoring

- Sensors: pH, nitrates, O2, temperature, turbidity
- Purpose: detect, and prevent water contamination
- Actions taken: warn people and authorities of an problem, very early before it affects public health
- Powering: batteries, power plug

8. Healtcare

- Sensors: hart rate, temperature, oxygen level, EKG, accelerometer
- Purpose: prevent and threat medical conditions
- Actions taken: alert doctor, family in case the person vital signs drop, or a mechanical accident occurs leaving the person unconscious, prevent disease before it happens 
- Powering: batteries, TEG, solar

All these usecases have something in common,  the data they produce.

Data can be visualized manually, and simple algorithms can scan it fast and prevent bad things from happening. 

But now with powerful machine learning algorithms we can go even further, we can run algorithms on large sets of gathered data, and they can analyze and learn subtle changes that lead to certain situation that we want to avoid. 
The algorithms will surpass our own understanding of data and find these helpful patterns. 

This means that after a system is deployed and sufficient data is gathered, all the users of the system will benefit from it afterwards. For example we may detect a stroke before it happens or find parking hotspots before they occur.



# Manually running project

Start rabbitmq, redis, mongodb 

````
python3 webserver.py --port 8080
python3 consummer.py --task store_momentary_data
python3 consummer.py --task rules_evaluator
````

# Running with docker-compose

````
cd project-directory/backend
docker-compose -f docker-services.yml -f docker-python.yml up -d

````
# Running ui

````
cd project-directory/ui
1. npm install
2. npm start - start dev webserver with livereload

````



# Databases
* RedisIo
  - for holding "locks"
* MongoDb
  - persist user, sensor, rule models
* Cassandra
  - long term storage
  - run jobs to digest the data