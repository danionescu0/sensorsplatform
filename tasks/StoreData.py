from repository.SensorsRepository import SensorsRepository
from model.Event import Event
from model.Sensor import Sensor

class StoreData():
    def __init__(self, sensors_repository: SensorsRepository) -> None:
        self.__sensors_repository = sensors_repository

    def run(self, event: Event):
        if event.name == 'sensor':
            self.__store_latest_sensor_data(event.model)

    def __store_latest_sensor_data(self, sensor: Sensor):
        self.__sensors_repository.update(sensor)

    def get_name(self):
        return 'store_data'