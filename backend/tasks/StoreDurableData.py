from logging import RootLogger

from model.Event import Event
from tasks.BaseTask import BaseTask

class StoreDurableData(BaseTask):
    def run(self, event: Event):
        self.__sensors_repository.update(event.model)
        sensor_persisted_event = Event(Event.TYPE_SENSOR_PERSISTED, event.model)
        self.__get_configured_async_jobs().publish(sensor_persisted_event)
        self.__logging.info("Event persisted with id: {0} and value {1}".format(event.model.id, event.model.latest_value))

    def get_name(self):
        return 'store_durable_data'

    def get_subscribed_event(self):
        return Event.TYPE_SENSOR_RECEIVED