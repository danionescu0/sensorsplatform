import statistics

from rules.parser.TokenConverter import TokenConverter
from rules.parser.Token import Token
from repository.SensorsRepository import SensorsRepository

class AverageSensorTokenConverter(TokenConverter):
    def __init__(self, sensors_repository: SensorsRepository) -> None:
        self.__sensors_repository = sensors_repository

    def get_value(self, token_raw_value: str):
        sensor_id = token_raw_value[0]
        values_to_count = token_raw_value[1]
        latest_values = self.__sensors_repository.get(sensor_id).latest
        if len(latest_values) < int(values_to_count):
            return 0 # hack. throw an error or smth

        return statistics.mean(latest_values[int(values_to_count):])

    def supports(self, token_type: str):
        if token_type == Token.TYPE_AVERAGE_SENSOR:
            return True

        return False