from datetime import datetime
from dateutil import tz

from rules.parser.TokenConverter import TokenConverter
from rules.parser.Token import Token

class CurrentTimeTokenConverter(TokenConverter):
    def get_value(self, token_raw_value: str):
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('Europe/Bucharest')
        initial_date = datetime.now().replace(tzinfo=from_zone)
        local_date = initial_date.astimezone(to_zone)

        return local_date.strftime('%H:%M')

    def supports(self, token_type: str):
        if token_type == Token.TYPE_CURRENT_TIME:
            return True

        return False