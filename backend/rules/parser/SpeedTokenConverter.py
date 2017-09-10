from geopy.distance import vincenty

from rules.parser.TokenConverter import TokenConverter
from rules.parser.Token import Token
from model.Sensor import Sensor
from repository.SensorsRepository import SensorsRepository
from rules.parser.ParseException import ParseException


class SpeedTokenConverter(TokenConverter):
    def __init__(self, sensors_repository: SensorsRepository) -> None:
        self.__sensors_repository = sensors_repository

    def get_value(self, token_raw_value: str):
        print('here')
        sensor = self.__sensors_repository.get(token_raw_value)

        if sensor.type != Sensor.TYPE_GIS:
            raise ParseException('Speed rule not allowed for sensor id: {0}'.format(token_raw_value))
        latest = sensor.latest
        if len(latest) < 2:
            return 0
        last = (float(latest[-1]['lat']), float(latest[-1]['lng']))
        one_before_last = (float(latest[-2]['lat']), float(latest[-2]['lng']))
        distance = vincenty(one_before_last, last).km

        return 0

    def supports(self, token_type: str):
        if token_type == Token.TYPE_SPEED:
            return True

        return False