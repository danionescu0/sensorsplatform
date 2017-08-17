import pika

class AsyncJobs:
    EXCHANGE_NAME = 'sensors'

    def __init__(self, host):
        self.__host = host
        self.__channel = None

    def connect(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host = self.__host))
        self.__channel = connection.channel()
        self.__channel.exchange_declare(exchange=self.EXCHANGE_NAME, type='fanout')

    def publish(self, sensor_data):
        self.__channel.basic_publish(exchange=self.EXCHANGE_NAME, routing_key ='', body = sensor_data)

    def consume(self, callback):
        result = self.__channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        self.__channel.queue_bind(exchange=self.EXCHANGE_NAME, queue=queue_name)
        self.__channel.basic_consume(callback,
                                     queue=queue_name,
                                     no_ack=True)
        self.__channel.start_consuming()