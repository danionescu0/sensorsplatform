from rules.parser.TokenConverter import TokenConverter
from rules.parser.Token import Token

class BooleanTokenConverter(TokenConverter):
    def get_value(self, token_raw_value: str):
            return {'True' : True, 'False' : False}[token_raw_value]

    def supports(self, token_type: str):
        if token_type == Token.TYPE_LITERAL_BOOLEAN:
            return True

        return False