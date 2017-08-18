import re
from datetime import datetime
from dateutil import tz
from typing import List

from rules.parser.Token import Token
from rules.parser.ParseException import ParseException

from repository.SensorsRepository import SensorsRepository

class Tokenizer:
    __token_rules = [
        ('S\[(\w+)\]', Token.TYPE_SENSOR),
        ('TIME', Token.TYPE_CURRENT_TIME),
        ('gt', Token.TYPE_EXPR_GREATER),
        ('lt', Token.TYPE_EXPR_LESS),
        ('btw', Token.TYPE_EXPR_BETWEEN),
        ('eq', Token.TYPE_EXPR_EQUAL),
        ('and', Token.TYPE_BOOLEAN_AND),
        ('or', Token.TYPE_BOOLEAN_OR),
        ('True|False', Token.TYPE_LITERAL_BOOLEAN),
        ('[0-9]{1,2}\:[0-9]{1,2}', Token.TYPE_LITERAL_TIME),
        ('\d+', Token.TYPE_LITERAL_INT),
    ]

    def __init__(self, sensors_repository: SensorsRepository) -> None:
        self.__sensors_repository = sensors_repository

    def tokenize(self, text:str) -> List[Token]:
        cleanned_text = self.__get_cleanned_text(text)

        return [self.__get_token(token_text) for token_text in cleanned_text.split()]

    def __get_cleanned_text(self, text):
        return re.sub('[(),]', ' ', text)

    def __get_token(self, token_text):
        for token_rule in self.__token_rules:
            found_matches = re.findall(token_rule[0], token_text)
            if not found_matches:
                continue
            return Token(token_rule[1], self.__get_token_value(token_rule[1], found_matches[0]))

        raise ParseException('Cannot parse symbol: {0}'.format(token_text))

    def __get_token_value(self, token_type, literal_value):
        if token_type == Token.TYPE_LITERAL_BOOLEAN:
            return {'True' : True, 'False' : False}[literal_value]
        elif token_type == Token.TYPE_LITERAL_INT:
            return int(literal_value)
        elif token_type == Token.TYPE_CURRENT_TIME:
            return self.__get_current_time()
        elif token_type == Token.TYPE_SENSOR:
            return self.__get_sensor_value(literal_value)

        return literal_value

    def __get_current_time(self):
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('Europe/Bucharest')
        initial_date = datetime.now().replace(tzinfo=from_zone)
        local_date = initial_date.astimezone(to_zone)

        return local_date.strftime('%H:%M')

    def __get_sensor_value(self, literal_value):
        return int(self.__sensors_repository.get(literal_value).latest_value)