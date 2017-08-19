from typing import List

class User:
    def __init__(self, userid: str, username: str, password: str , email: str, phone: str, sensor_ids: List[int]) -> None:
        self.userid = userid
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.sensor_ids = sensor_ids