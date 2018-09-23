from logging import RootLogger

from repository.SensorsRepository import SensorsRepository
from model.Event import Event
from tasks.BaseTask import BaseTask


class StoreDurableData(BaseTask):
    def __init__(self, sensors_repository: SensorsRepository,  logging: RootLogger) -> None:
        self.__sensors_repository = sensors_repository
        self.__logging = logging

    def run(self, event: Event):
        self.__logging.debug("will store durable data")

    def get_name(self):
        return 'store_durable_data'

    def get_subscribed_event(self):
        return Event.TYPE_SENSOR_RECEIVED