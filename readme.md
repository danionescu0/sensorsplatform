
#Manually running project

Start rabbitmq, redis, mongodb 

````
python3 webserver.py --port 8080
python3 consummer.py --task store_momentary_data
python3 consummer.py --task rules_evaluator
````

#Running with docker-compose

````
cd project-directory/backend
docker-compose -f docker-services.yml -f docker-python.yml up -d

````
#Running ui

````
cd project-directory/ui
1. npm install
2. npm start - start dev webserver with livereload

````

#Todo list
* ui server with docker
* added small demos for rules in UI
* create a rule that work for many sensors of same type like ANY(S1, S2,..Sn)

#Bug list
* fix docker python containers time.sleep issue

#Databases
* RedisIo
  - for holding "locks"
* MongoDb
  - persist user, sensor, rule models
* Cassandra
  - long term storage
  - run jobs to digest the data
