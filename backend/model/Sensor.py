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
        self._name = None
        self._gis = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def gis(self) -> Tuple[float, float]:
        return self._gis

    @gis.setter
    def gis(self, value: Tuple[float, float]):
        self._gis = value

    def to_mongo_doc(self):
        doc = self.__dict__
        gis = doc.get("_gis")
        doc["name"] = doc.get("_name")
        doc["gis"] = {"lat": gis[0], "lng": gis[1]}
        doc.pop("_name")
        doc.pop("_gis")

        return doc
