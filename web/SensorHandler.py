import tornado.web

class SensorHandler(tornado.web.RequestHandler):
    def initialize(self, sensor_publisher):
        self.__sensor_publisher = sensor_publisher

    def put(self):
        self.set_status(200)
        print(self.request.body)
        print('put')
        self.__sensor_publisher.publish(self.request.body)