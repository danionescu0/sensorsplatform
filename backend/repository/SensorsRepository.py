import time
from typing import List

from bson.objectid import ObjectId

from model.Sensor import Sensor
from repository.AbstractMongoRepository import AbstractMongoRepository


class SensorsRepository(AbstractMongoRepository):
    COLLECTION_NAME = 'sensors'
    VALUES_TO_KEEP = 50

    def __init__(self, host_uri: str) -> None:
        super(SensorsRepository, self).__init__(host_uri)

    def get(self, id: str) -> Sensor:
        result = self.__hidrate(self.find({"_id" : ObjectId(id)}))
        if len(result) == 0:
            return None

        return result[0]

    def get_batch(self, ids: list) -> List[Sensor]:
        object_ids = [ObjectId(id) for id in ids]

        return self.__hidrate(self.find({"_id": {'$in': object_ids}}))

    def create(self, sensor: Sensor) -> str:
        return self.get_collection().insert_one(sensor.to_mongo_doc()).inserted_id

    def update(self, sensor: Sensor):
        update_data = {
            "$set" : {
                "type": sensor.type,
                "latest_value": sensor.latest_value,
            },
            "$push" : {
                "latest": {
                    "$each": [{"value": sensor.latest_value, "timestamp": time.time()}],
                    "$sort": {"timestamp": 1},
                    "$slice": -1 * self.VALUES_TO_KEEP
                }
            }
        }
        self.get_collection().update_one({"_id": ObjectId(sensor.id)}, update_data, True)

    def __hidrate(self, raw_data):
        sensors = []

        for data in raw_data:
            latest = [(latest['timestamp'], latest['value']) for latest in data['latest']]
            sensor = Sensor(str(data['_id']), data['type'], data['latest_value'], latest)
            sensor.name = data['name']
            sensor.gis = (float(data['gis']['lat']), float(data['gis']['lng']))
            sensors.append(sensor)

        return sensors