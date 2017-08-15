import pika

class Sensors:
    QUEUE_NAME = 'sensors'

    def __init__(self, host):
        self.__host = host
        self.__channel = None

    def connect(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host = self.__host))
        self.__channel = connection.channel()
        self.__channel.queue_declare(queue = self.QUEUE_NAME)

    def publish(self, sensor_data):
        self.__channel.basic_publish(exchange='', routing_key = self.QUEUE_NAME, body = sensor_data)

    def consume(self, callback):
        self.__channel.basic_consume(callback,
                              queue=self.QUEUE_NAME,
                              no_ack=True)
        self.__channel.start_consuming()
