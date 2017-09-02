import json
from logging import RootLogger

import tornado.web

from model.Event import Event
from model.Sensor import Sensor
from services.AsyncJobs import AsyncJobs


class SensorHandler(tornado.web.RequestHandler):
    def initialize(self, async_jobs: AsyncJobs, logging: RootLogger):
        self.__async_jobs = async_jobs
        self.__logging = logging

    def put(self, id):
        self.set_status(200)
        sensor_data = json.loads(self.request.body.decode("utf-8"))
        self.__logging.debug('Sensor data received: '.format(self.request.body.decode("utf-8")))
        sensor = Sensor(id, sensor_data['type'], float(sensor_data['value']), None)
        event = Event(Event.TYPE_SENSOR_RECEIVED, sensor)
        self.__async_jobs.publish(event)