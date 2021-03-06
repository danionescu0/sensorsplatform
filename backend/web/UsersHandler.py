import json

from model.User import User
from repository.UsersRepository import UsersRepository
from security.secure import secure
from web.CorsHandler import CorsHandler


class UsersHandler(CorsHandler):

    def initialize(self, users_repo: UsersRepository):
        self.__users_repo = users_repo

    @secure
    def get(self, user_id):
        user = self.__users_repo.get_by_id(user_id)
        if not user:
            self.set_status(404)
            return

        self.write(json.dumps(user.get_object_dict_without_key("password")))

    def post(self):
        data = json.loads(self.request.body.decode("utf-8"))
        user = User(data['first_name'], data['last_name'], data['password'], data['email'], data['phone'], [])

        self.__users_repo.create(user)
        self.set_status(201)