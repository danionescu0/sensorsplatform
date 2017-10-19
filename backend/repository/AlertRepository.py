from typing import List

from repository.AbstractMongoRepository import AbstractMongoRepository
from model.Alert import Alert


class AlertRepository(AbstractMongoRepository):
    COLLECTION_NAME = 'alerts'

    def __init__(self, host_uri: str) -> None:
        super(AlertRepository, self).__init__(host_uri)

    def create(self, alert: Alert) -> str:
        alert_mongodb_model = alert.__dict__
        alert_mongodb_model.pop('id', None)

        return self.get_collection().insert_one(alert_mongodb_model).inserted_id

    def get_for_user(self, userid: str, limit: int) -> List[Alert]:
        data = self.get_collection()\
                    .find({'userid' : userid})\
                    .sort([('timestamp', -1)])\
                    .limit(limit)

        return self.__hidrate(data)

    def __hidrate(self, raw_data):
        alerts = []
        for data in raw_data:
            rule = Alert(str(data['_id']), data['userid'], data['rule_id'], data['timestamp'])
            alerts.append(rule)

        return alerts