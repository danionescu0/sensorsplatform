import json

import tornado.web

from model.Sensor import Sensor
from repository.SensorsRepository import SensorsRepository
from repository.UsersRepository import UsersRepository
from security.secure import secure


@secure
class SensorsHandler(tornado.web.RequestHandler):
    def initialize(self, sensors_repo: SensorsRepository, users_repo: UsersRepository):
        self.__sensors_repo = sensors_repo
        self.__users_repo = users_repo

    def get(self, userId):
        user = self.__users_repo.get_by_id(userId)
        if not user:
            self.set_status(404)
            return

        sensors = [sensor.__dict__ for sensor in self.__sensors_repo.get_batch(user.sensor_ids)]
        self.write(json.dumps(sensors))

    def post(self, userId):
        data = json.loads(self.request.body.decode("utf-8"))
        sensor = Sensor(None, data['type'], 0, [])
        sensor_id = self.__sensors_repo.create(sensor)
        self.__users_repo.add_sensor_id(userId, str(sensor_id))
        self.set_status(201)
