from logging import RootLogger

from repository.SensorsRepository import SensorsRepository
from model.Event import Event
from tasks.BaseTask import BaseTask
from services.AsyncJobs import AsyncJobs


class StoreMomentaryData(BaseTask):
    def __init__(self, sensors_repository: SensorsRepository, async_jobs: AsyncJobs, logging: RootLogger) -> None:
        self.__sensors_repository = sensors_repository
        self.__async_jobs = async_jobs
        self.__logging = logging
        self.__configured_async_jobs = None

    def __get_configured_async_jobs(self):
        if None is not self.__configured_async_jobs:
            return self.__configured_async_jobs
        self.__async_jobs.register_event(Event.TYPE_SENSOR_PERSISTED)
        self.__configured_async_jobs = self.__async_jobs

        return self.__configured_async_jobs

    def run(self, event: Event):
        self.__sensors_repository.update(event.model)
        sensor_persisted_event = Event(Event.TYPE_SENSOR_PERSISTED, event.model)
        self.__get_configured_async_jobs().publish(sensor_persisted_event)
        self.__logging.info("Event persisted with id: {0} and value {1}".format(event.model.id, event.model.latest_value))

    def get_name(self):
        return 'store_momentary_data'

    def get_subscribed_event(self):
        return Event.TYPE_SENSOR_RECEIVED