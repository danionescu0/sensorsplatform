from rules.parser.TokenConverter import TokenConverter
from rules.parser.Token import Token
from repository.SensorsRepository import SensorsRepository

class SensorTokenConverter(TokenConverter):
    def __init__(self, sensors_repository: SensorsRepository) -> None:
        self.__sensors_repository = sensors_repository

    def get_value(self, token_raw_value: str):
        return int(self.__sensors_repository.get(token_raw_value).latest_value)

    def supports(self, token_type: str):
        if token_type == Token.TYPE_SENSOR:
            return True

        return False