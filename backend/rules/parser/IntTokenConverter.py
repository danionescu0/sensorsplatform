from rules.parser.TokenConverter import TokenConverter
from rules.parser.Token import Token


class IntTokenConverter(TokenConverter):
    def get_value(self, token_raw_value: str):
        return int(token_raw_value)

    def get_supported_token(self) -> str:
        return Token.TYPE_LITERAL_INT