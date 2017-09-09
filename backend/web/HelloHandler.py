import tornado

from security.secure import secure


@secure
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")