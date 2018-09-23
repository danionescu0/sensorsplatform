from repository.UsersRepository import UsersRepository
from security.JwtTokenFactory import JwtTokenFactory
from web.CorsHandler import CorsHandler


class AuthHandler(CorsHandler):
    def initialize(self, users_repo: UsersRepository, token_factory: JwtTokenFactory):
        self.__users_repo = users_repo
        self.__token_factory = token_factory

    def post(self):
        email = self.get_argument("email")
        user = self.__users_repo.get_by_email(email)
        if user == None:
            self.set_status(403)
            self.write("Wrong email!")
            return
        password = self.get_argument("password")
        if user.password != password:
            self.set_status(403)
            self.write("Bad password!")
            return

        self.write(self.__token_factory.create(user.userid))