from geopy.distance import vincenty

from rules.parser.TokenConverter import TokenConverter
from rules.parser.Token import Token
from model.Sensor import Sensor
from repository.SensorsRepository import SensorsRepository
from rules.parser.ParseException import ParseException


class GisDistanceTokenConverter(TokenConverter):
    def __init__(self, sensors_repository: SensorsRepository) -> None:
        self.__sensors_repository = sensors_repository

    def get_value(self, token_raw_value: str):
        sensor_id, rule_latitide, rule_longitude = token_raw_value.split(':', 3)
        sensor = self.__sensors_repository.get(sensor_id)

        if sensor.type != Sensor.TYPE_GIS:
            raise ParseException('Gis distance not allowed for sensor id: {0}'.format(sensor_id))
        current_coordonates = (float(sensor.latest_value['lat']), float(sensor.latest_value['lng']))
        rule_coordonates = (float(rule_latitide), float(rule_longitude))

        return vincenty(current_coordonates, rule_coordonates).km

    def supports(self, token_type: str):
        if token_type == Token.TYPE_GIS_DISTANCE:
            return True

        return False