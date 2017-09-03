from rules.parser.TokenConverter import TokenConverter
from rules.parser.Token import Token
from model.Sensor import Sensor
from repository.SensorsRepository import SensorsRepository


class SensorTokenConverter(TokenConverter):
    def __init__(self, sensors_repository: SensorsRepository) -> None:
        self.__sensors_repository = sensors_repository

    def get_value(self, token_raw_value: str):
        sensor = self.__sensors_repository.get(token_raw_value)
        if sensor.type == Sensor.TYPE_GIS:
            return float(sensor.latest_value['lat']), float(sensor.latest_value['lng'])

        return float(sensor.latest_value)

    def supports(self, token_type: str):
        if token_type == Token.TYPE_SENSOR:
            return True

        return False