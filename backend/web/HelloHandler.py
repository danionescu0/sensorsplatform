from security.secure import secure
from web.CorsHandler import CorsHandler


@secure
class HelloHandler(CorsHandler):
    def get(self):
        self.write("Hello, world")

    def options(self):
        print('aaaaa')