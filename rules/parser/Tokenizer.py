import re
from typing import List

from rules.parser.Token import Token
from rules.parser.ParseException import ParseException
from rules.parser.TokenConverter import TokenConverter

class Tokenizer:
    token_converters = []

    __token_rules = [
        ('S\[(\w+)\]', Token.TYPE_SENSOR),
        ('S_AVG\[(\d+)\:(\d+)]', Token.TYPE_AVERAGE_SENSOR),
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

    def tokenize(self, text:str) -> List[Token]:
        cleanned_text = self.__get_cleanned_text(text)

        return [self.__get_token(token_text) for token_text in cleanned_text.split()]

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

        raise ParseException('Cannot parse symbol: {0}'.format(token_text))

    def __get_token_value(self, token_type: str, token_raw_value: str):
        token_converter = [converter for converter in self.token_converters if converter.supports(token_type)]
        if 1 != len(token_converter):
            return token_raw_value
        token_converter = token_converter[0]

        return token_converter.get_value(token_raw_value)