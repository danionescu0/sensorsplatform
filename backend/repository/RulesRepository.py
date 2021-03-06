from typing import List

from bson.objectid import ObjectId

from repository.AbstractMongoRepository import AbstractMongoRepository
from model.Rule import Rule


class RulesRepository(AbstractMongoRepository):
    COLLECTION_NAME = 'rules'

    def __init__(self, host_uri: str) -> None:
        super(RulesRepository, self).__init__(host_uri)

    def get_for_user(self, userid: str) -> List[Rule]:
        return self.__hidrate(self.get_collection().find({'userid' : userid}))

    def get(self, id: str) -> Rule:
        return self.__hidrate(self.get_collection().find({'_id' : ObjectId(id)}))[0]

    def create(self, rule: Rule) -> None:
        self.get_collection().insert_one(rule.to_mongo_doc())

    def __hidrate(self, raw_data):
        rules = []
        for element in raw_data:
            rule = Rule(str(element['_id']), element['userid'], element['name'], element['rule_text'], element['triggers'])
            rule.trigger_min_interval = self.default_val(element, 'trigger_min_interval', 0)
            rules.append(rule)

        return rules