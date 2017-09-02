import time
import argparse

import tornado.ioloop
import tornado.web

from container import Container
from web.SensorHandler import SensorHandler
from model.Event import Event

container = Container()

file = open("testfile.txt", "w")
file.write("cici bibi")
file.close()


time.sleep(10)
print('cici')

async_jobs = container.get('async_jobs')
async_jobs.register_event(Event.TYPE_SENSOR_RECEIVED)
logging = container.get('logging')
print('cici2')

def make_app():
    return tornado.web.Application([
        (
            r"/sensor/(\d*)", SensorHandler,
            dict(async_jobs = async_jobs, logging = logging)
        ),
    ])

parser = argparse.ArgumentParser(description='Port')
parser.add_argument('--port', dest='port', type=str, default=8080)
args = parser.parse_args()

if __name__ == "__main__":
    app = make_app()
    app.listen(args.port, '0.0.0.0')
    tornado.ioloop.IOLoop.current().start()