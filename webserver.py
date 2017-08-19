import tornado.ioloop
import tornado.web

from container import Container
from web.SensorHandler import SensorHandler

container = Container()

sensors_repo = container.get('async_jobs')
sensors_repo.connect()

def make_app():
    return tornado.web.Application([
        (
            r"/sensor/(\d*)", SensorHandler,
            dict(async_jobs = sensors_repo)
        ),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()