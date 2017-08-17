#Todo list

* a limit system for alerts (max 1 per minute or hour etc)


#Mongodb

> use multi_sensor_platform
switched to db multi_sensor_platform
> db.rules.insert({"userid": 1, "rule_text" : "and  ( eq(TIME, '8:05'), gt(20, 40) )", "triggers" : ["send_alert","sms"]})

#Running composer

````
cd docker-container
docker-compose up
````