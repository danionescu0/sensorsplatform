from model.Sensor import Sensor

class SensorsRepository():

    def get_latest(self, userid: str):
        return [Sensor("4", 'temperature', '12.3'), Sensor("4", 'humidity', '12.3')]

    def get(self, id: str) -> Sensor:
        return Sensor(id, 'temperature', '12')

    def override(self, sensor: Sensor):
        pass