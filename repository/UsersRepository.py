from bson.objectid import ObjectId

from model.User import User
from repository.AbstractMongoRepository import AbstractMongoRepository

class UsersRepository(AbstractMongoRepository):
    COLLECTION_NAME = 'users'

    def __init__(self, host_uri: str) -> None:
        super(UsersRepository, self).__init__(host_uri)

    def get_by_sensor_id(self, id: str) -> User:
        result = self.__hidrate(self.get_collection().find({"sensor_ids" : {"$in": [id]}}))
        if len(result) == 0:
            return None

        return result[0]

    def get_by_email(self, email: str) -> User:
        result = self.__hidrate(self.find({"email": email}))
        if len(result) == 0:
            return None

        return result[0]

    def get_by_id(self, id: str) -> User:
        result = self.__hidrate(self.find({"_id": ObjectId(id)}))
        if len(result) == 0:
            return None

        return result[0]

    def create(self, user: User) -> None:
        self.get_collection().insert_one(user.__dict__)

    def __hidrate(self, raw_data):
        users = []
        for element in raw_data:
            user = User(element['username'], element['password'], element['email'], element['phone'],
                 element['sensor_ids'])
            user.set_userid(str(element['_id']))
            users.append(user)

        return users