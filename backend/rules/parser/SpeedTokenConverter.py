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
        sensor = self.__sensors_repository.get(token_raw_value)

        if sensor.type != Sensor.TYPE_GIS:
            raise ParseException('Speed rule not allowed for sensor id: {0}'.format(token_raw_value))
        latest = sensor.latest
        if len(latest) < 2:
            return 0
        last = (float(latest[-1][1]['lat']), float(latest[-1][1]['lng']))
        one_before_last = (float(latest[-2][1]['lat']), float(latest[-2][1]['lng']))
        time_difference = latest[-1][0] - latest[-2][0]
        distance = vincenty(one_before_last, last).km

        return round(distance / (time_difference/3600), 2)

    def get_supported_token(self) -> str:
        return Token.TYPE_SPEED