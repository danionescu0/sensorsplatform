import json

from model.User import User
from repository.UsersRepository import UsersRepository
from security.secure import secure
from web.CorsHandler import CorsHandler


class UsersHandler(CorsHandler):

    def initialize(self, users_repo: UsersRepository):
        self.__users_repo = users_repo

    @secure
    def get(self, userId):
        user = self.__users_repo.get_by_id(userId)
        if not user:
            self.set_status(404)
            return
        user_dict = user.__dict__
        user_dict.pop('password')

        self.write(json.dumps(user_dict))

    def post(self):
        data = json.loads(self.request.body.decode("utf-8"))
        user = User(data['first_name'], data['last_name'], data['password'], data['email'], data['phone'], [])

        self.__users_repo.create(user)
        self.set_status(201)