from typing import List

class User:
    def __init__(self, first_name: str,  last_name: str, password: str , email: str, phone: str, sensor_ids: List[int]) -> None:
        self.userid = None
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.phone = phone
        self.sensor_ids = sensor_ids

    def set_userid(self, userid: str) -> None:
        self.userid = userid