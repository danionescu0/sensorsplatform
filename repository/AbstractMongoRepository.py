
from pymongo import MongoClient

class AbstractMongoRepository():
    DATABASE_NAME = 'multi_sensor_platform'

    def __init__(self, host_uri: str) -> None:
        self.__host_uri = host_uri
        self.__collection = None

    def get_collection(self):
        if None != self.__collection:
            return self.__collection

        client = MongoClient(self.__host_uri)
        self.__collection = client[self.DATABASE_NAME][self.COLLECTION_NAME]

        return self.__collection