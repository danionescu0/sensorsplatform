import time
from model.Sensor import Sensor
from repository.AbstractMongoRepository import AbstractMongoRepository

class SensorsRepository(AbstractMongoRepository):
    COLLECTION_NAME = 'sensors'
    VALUES_TO_KEEP = 10

    def __init__(self, host_uri: str) -> None:
        super(SensorsRepository, self).__init__(host_uri)

    def get(self, id: str) -> Sensor:
        result = self.__hidrate(self.get_collection().find({"id" : id}))
        if len(result) == 0:
            return None

        return result[0]

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
        self.get_collection().update_one({"id": sensor.id}, update_data, True)

    def __hidrate(self, raw_data):
        parsed = []
        for data in raw_data:
            data['latest'] = [latest['value'] for latest in data['latest']]
            parsed.append(data)

        return [
            Sensor(element['id'], element['type'], element['latest_value'], element['latest'])
            for element in parsed
        ]