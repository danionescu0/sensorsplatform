from datetime import datetime
from datetime import timedelta

import jwt


class JwtTokenFactory:

    def __init__(self, jwt_secret: str) -> None:
        self.__jwt_secret = jwt_secret

    def create(self, userid: str) -> str:
        payload = {
            'userid': userid,
            'exp': datetime.utcnow() + timedelta(days=1)
        }

        return jwt.encode(payload, self.__jwt_secret, algorithm='HS256')