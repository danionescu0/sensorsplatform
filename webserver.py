import time
import argparse

import tornado.ioloop
import tornado.web

from container import Container
from web.HelloHandler import HelloHandler
from web.AuthHandler import AuthHandler
from web.SensorHandler import SensorHandler
from model.Event import Event
from web.UsersHandler import UsersHandler

container = Container()

time.sleep(5)
async_jobs = container.get('async_jobs')
async_jobs.register_event(Event.TYPE_SENSOR_RECEIVED)
logging = container.get('logging')
users_repo = container.get('users_repository')
jwt_token_factory = container.get('jwt_token_factory')

def make_app():
    return tornado.web.Application([
        (
            r"/sensor/(\d*)", SensorHandler,
            dict(async_jobs = async_jobs, logging = logging)
        ),
        (r"/auth", AuthHandler, dict(users_repo = users_repo, token_factory = jwt_token_factory)),
        (r"/users", UsersHandler, dict(users_repo = users_repo)),
        (r"/users/(.*)", UsersHandler, dict(users_repo = users_repo)),
        (r"/hello", HelloHandler)
    ])

parser = argparse.ArgumentParser(description='Port')
parser.add_argument('--port', dest='port', type=str, default=8080)
args = parser.parse_args()

if __name__ == "__main__":
    app = make_app()
    app.listen(args.port, '0.0.0.0')
    tornado.ioloop.IOLoop.current().start()