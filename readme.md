
#Manually running project

Start rabbitmq, redis, mongodb 

````
python3 webserver.py --port 8080
python3 consummer.py --task store_data
python3 consummer.py --task rules_evaluator
````

#Running with docker-compose

````
cd docker-container
docker-compose up --build
````

#Todo list
* build a web interface
* add more rules components
* add Sensor GPS data   
* add rules that work with GPS data: distance, speed

#Bug list
* fix timeout situations
* fix docker python containers time.sleep issue

#Databases
* RedisIo
  - for holding "locks"
* MongoDb
  - persist user, sensor, rule models
* Cassandra
  - long term storage
  - run jobs to digest the data
