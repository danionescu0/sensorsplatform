#Todo list

* a limit system for alerts (max 1 per minute or hour etc)
* 


#Docker
* docker run  -p 5672:5672 rabbitmq


#Mongodb

> use multi_sensor_platform
switched to db multi_sensor_platform
> db.rules.insert({"userid": 4, "rule_text" : "and  ( eq(S[phoneIsHome:False], True), gt(S[airPollution:living], 40) )", "triggers" : ["email","sms"]})
