#Todo list

* a limit system for alerts (max 1 per minute or hour etc)


#Mongodb

> use multi_sensor_platform
switched to db multi_sensor_platform
db.rules.insert({"userid": 1, "rule_text" : "and  ( eq(TIME, '8:05'), gt(20, 40) )", "triggers" : ["send_alert","sms"]})
db.users.insert({ "_id" : { "$oid" : "599868bb677e0457a9137039" }, "id" : 1.0, "username" : "danionescu", "password" : "testpass", "email" : "test@test.com", "phone" : "0726775455", "sensors" : [ 1.0, 2.0, 5.0 ] })

#Running composer

````
cd docker-container
docker-compose up
````