import tornado.ioloop
import tornado.web

from web.SensorHandler import SensorHandler
from repository.Sensors import Sensors
import config

sensors_repo = Sensors(config.rabbitmq_host)
sensors_repo.connect()

def make_app():
    return tornado.web.Application([
        (
            r"/sensor/\d*", SensorHandler,
            dict(sensor_publisher = sensors_repo)
        ),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()