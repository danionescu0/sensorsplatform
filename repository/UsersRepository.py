from model.User import User
from repository.AbstractMongoRepository import AbstractMongoRepository

class UsersRepository(AbstractMongoRepository):
    COLLECTION_NAME = 'users'

    def __init__(self, host_uri: str) -> None:
        super(UsersRepository, self).__init__(host_uri)

    def get_by_sensor_id(self, id: str) -> User:
        result = self.__hidrate(self.get_collection().find({"sensors" : {"$in": [id]}}))
        if len(result) == 0:
            return None

        return result[0]

    def get_by_email(self, email: str) -> User:
        result = self.__hidrate(self.get_collection().find({"email": email}))
        if len(result) == 0:
            return None

        return result[0]

    def __hidrate(self, raw_data):
        return [
            User(element['id'], element['username'], element['password'], element['email'],  element['phone'],
                 element['sensors'])
            for element in raw_data
        ]