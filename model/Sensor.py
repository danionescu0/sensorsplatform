from typing import List

class Sensor():
    TYPE_HUMIDITY = 'humidity'
    TYPE_TEMPERATURE = 'temperature'
    TYPE_LIGHT = 'light'
    TYPE_AIR_PRESSURE = 'air_pressure'
    TYPE_GIS = 'gis_coordonates'

    def __init__(self, id: str, type: str, latest_value: float, latest: List[float]) -> None:
        self.id = id
        self.type = type
        self.latest_value = latest_value
        self.latest = latest