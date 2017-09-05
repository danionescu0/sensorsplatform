import jwt
from datetime import datetime
from datetime import timedelta


class JwtTokenFactory:
    SECRET = 'n1cusord3labraila'

    def create(self, userid: str) -> str:
        payload = {
            'userid': userid,
            'exp': datetime.utcnow() + timedelta(days=1)
        }

        return jwt.encode(payload, self.SECRET, algorithm='HS256')
