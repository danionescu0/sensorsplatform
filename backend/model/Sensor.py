from typing import List
from typing import Tuple

class Sensor():
    TYPE_HUMIDITY = 'humidity'
    TYPE_TEMPERATURE = 'temperature'
    TYPE_LIGHT = 'light'
    TYPE_AIR_PRESSURE = 'air_pressure'
    TYPE_GIS = 'gis'

    def __init__(self, id: str, type: str, latest_value: float, latest: List[Tuple]) -> None:
        self.id = id
        self.type = type
        self.latest_value = latest_value
        self.latest = latest