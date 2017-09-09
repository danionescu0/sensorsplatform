import json

import tornado

from model.User import User
from repository.UsersRepository import UsersRepository
from security.secure import secure


@secure
class UsersHandler(tornado.web.RequestHandler):

    def initialize(self, users_repo: UsersRepository):
        self.__users_repo = users_repo

    def get(self, userId):
        user = self.__users_repo.get_by_id(userId)
        if user == None:
            self.set_status(404)
            return
        userDict = user.__dict__
        userDict.pop('password')

        self.write(json.dumps(userDict))

    def post(self):
        data = json.loads(self.request.body.decode("utf-8"))
        user = User(data['username'], data['password'], data['email'], data['phone'], [])

        self.__users_repo.create(user)
        self.set_status(201)