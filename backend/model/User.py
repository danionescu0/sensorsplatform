from typing import List

class User:
    def __init__(self, first_name: str,  last_name: str, password: str , email: str, phone: str, sensor_ids: List[int]) -> None:
        self._userid = None
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.phone = phone
        self.sensor_ids = sensor_ids

    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, value):
        self._userid = value

    def to_mongo_doc(self):
        return self.get_object_dict_without_key("_userid")

    def get_object_dict_without_key(self, key: str) -> dict:
        self_dict = self.__dict__
        self_dict.pop(key)

        return self_dict
