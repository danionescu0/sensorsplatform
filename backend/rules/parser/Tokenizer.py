import re
from typing import List

from rules.parser.Token import Token
from rules.parser.ParseException import ParseException
from rules.parser.TokenConverter import TokenConverter


class Tokenizer:
    token_converters = []

    def __init__(self, logging) -> None:
        self.__logging = logging

    __token_rules = [
        # S[id]
        ('S\[(\w+)\]', Token.TYPE_SENSOR),
        # S_AVG[id, last positions] don't know if this works
        ('S_AVG\[(\w+)\:(\d+)]', Token.TYPE_AVERAGE_NUMERICAL_SENSOR),
        # SPEED[id]
        ('SPEED\[(\w+)\]', Token.TYPE_SPEED),
        # GIS_DST[id, gis_lng, gis_lat]
        ('GIS_DST\[(\w+\:[0-9.]{1,10}\:[0-9.]{1,10})\]', Token.TYPE_GIS_DISTANCE),
        ('TIME', Token.TYPE_CURRENT_TIME),
        ('gt', Token.TYPE_EXPR_GREATER),
        ('lt', Token.TYPE_EXPR_LESS),
        ('btw', Token.TYPE_EXPR_BETWEEN),
        ('eq', Token.TYPE_EXPR_EQUAL),
        ('and', Token.TYPE_BOOLEAN_AND),
        ('or', Token.TYPE_BOOLEAN_OR),
        ('True|False', Token.TYPE_LITERAL_BOOLEAN),
        # HH:mm
        ('[0-9]{1,2}\:[0-9]{1,2}', Token.TYPE_LITERAL_TIME),
        ('\d+', Token.TYPE_LITERAL_INT),
    ]

    def tokenize(self, text:str) -> List[Token]:
        return [self.__get_token(token_text) for token_text in self.__get_cleanned_text(text).split()]

    def add_token_converter(self, token_converter: TokenConverter):
        self.token_converters.append(token_converter)

    def __get_cleanned_text(self, text: str):
        return re.sub('[(),]', ' ', text)

    def __get_token(self, token_text: str) -> Token:
        for token_rule in self.__token_rules:
            found_matches = re.findall(token_rule[0], token_text)
            if not found_matches:
                continue

            return Token(token_rule[1], self.__get_token_value(token_rule[1], found_matches[0]))

        raise ParseException('Cannot parse token symbol: {0}'.format(token_text))

    def __get_token_value(self, token_type: str, token_raw_value: str):
        token_converter = [converter for converter in self.token_converters if converter.get_supported_token() == token_type]
        if 1 != len(token_converter):
            return token_raw_value
        token_converter = token_converter[0]
        value = token_converter.get_value(token_raw_value)

        return value