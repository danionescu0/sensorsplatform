import pika
import pickle

from model.Event import Event

class AsyncJobs:
    def __init__(self, host) -> None:
        self.__host = host
        self.__channel = None
        self.__event_name = None

    def register_event(self, event_name: str):
        self.__event_name = event_name
        self.__do_register_event()

    def __do_register_event(self):
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.__host, port=5672, heartbeat_interval=120)
        )
        self.__channel = self.__connection.channel()
        self.__channel.exchange_declare(exchange=self.__event_name, exchange_type='fanout')

    def publish(self, event: Event) -> None:
        if not self.__connection.is_open:
            self.__do_register_event()
        self.__channel.basic_publish(exchange=event.name, routing_key ='', body = pickle.dumps(event))

    def consume(self, callback) -> None:
        if None is self.__event_name:
            raise Exception("Use register_event first to register an event name")
        result = self.__channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        self.__channel.queue_bind(exchange=self.__event_name, queue=queue_name)
        self.__channel.basic_consume(callback,
                                     queue=queue_name,
                                     no_ack=True)
        self.__channel.start_consuming()