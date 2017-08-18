from model.Sensor import Sensor

class SensorsRepository():
    def get_latest(self, userid: int):
        return [Sensor(4, 'temperature', '12.3'), Sensor(4, 'humidity', '12.3')]

    def get(self, id: int) -> Sensor:
        return Sensor(id, 'temperature', '12')