import time
import argparse

import tornado.ioloop
import tornado.web

from container import Container
from model.Event import Event
from web.SensorsHandler import SensorsHandler
from web.AuthHandler import AuthHandler
from web.SensorEventHandler import SensorEventHandler
from web.UsersHandler import UsersHandler
from web.AlertsHandler import AlertsHandler

container = Container()

time.sleep(5)
async_jobs = container.get('async_jobs')
async_jobs.register_event(Event.TYPE_SENSOR_RECEIVED)
logging = container.get('logging')
users_repo = container.get('users_repository')
alerts_repo = container.get('alerts_repository')
sensors_repo = container.get('sensors_repository')
rules_repo = container.get('rules_repository')
jwt_token_factory = container.get('jwt_token_factory')

def make_app():
    return tornado.web.Application([
        (
            r"/sensor/(\w*)", SensorEventHandler,
            dict(async_jobs = async_jobs, logging = logging)
        ),
        (r"/auth", AuthHandler, dict(users_repo=users_repo, token_factory=jwt_token_factory)),
        (r"/user-sensors/(.*)", SensorsHandler, dict(sensors_repo=sensors_repo, users_repo=users_repo)),
        (r"/alerts/user/(.*)", AlertsHandler, dict(alerts_repo=alerts_repo, rules_repo=rules_repo, users_repo=users_repo)),
        (r"/users", UsersHandler, dict(users_repo=users_repo)),
        (r"/users/(.*)", UsersHandler, dict(users_repo=users_repo)),
    ])

parser = argparse.ArgumentParser(description='Port')
parser.add_argument('--port', dest='port', type=str, default=8080)
args = parser.parse_args()

if __name__ == "__main__":
    app = make_app()
    app.listen(args.port, '0.0.0.0')
    tornado.ioloop.IOLoop.current().start()