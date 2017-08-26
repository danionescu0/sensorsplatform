
#Manually running project
````
python3 webserver.py --port 8080
python3 consummer.py --task store_data
python3 consummer.py --task rules_evaluator
````

#Todo list
* add logging
* build a web interface
* add more rules components

#Databases
* RedisIo
  - for holding "locks"
* MongoDb
  - persist user, sensor, rule models
* Cassandra
  - long term storage
  - run jobs to digest the data


#Running composer

````
cd docker-container
docker-compose up
````