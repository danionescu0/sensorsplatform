from pymongo import MongoClient

from model.Rule import Rule

class RulesRepository():
    DATABASE_NAME = 'multi_sensor_platform'
    COLLECTION_NAME = 'rules'

    def __init__(self, host_uri: str) -> None:
        self.__host_uri = host_uri
        self.__collection = None

    def get_for_user(self, userid: int):
        return self.__hidrate(self.__get_collection().find({'userid' : userid}))

    def __get_collection(self):
        if None != self.__collection:
            return self.__collection

        client = MongoClient(self.__host_uri)
        self.__collection = client[self.DATABASE_NAME][self.COLLECTION_NAME]

        return self.__collection

    def __hidrate(self, raw_data):
        return [Rule(element['userid'], element['rule_text'], element['triggers']) for element in raw_data]