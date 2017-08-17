from model.Sensor import Sensor

class SensorsRepository():
    def get_latest(self, id):
        return Sensor(id, 'temperature', '12.3')