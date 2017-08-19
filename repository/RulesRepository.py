from repository.AbstractMongoRepository import AbstractMongoRepository
from model.Rule import Rule

class RulesRepository(AbstractMongoRepository):
    COLLECTION_NAME = 'rules'

    def __init__(self, host_uri: str) -> None:
        super(RulesRepository, self).__init__(host_uri)

    def get_for_user(self, userid: str):
        return self.__hidrate(self.get_collection().find({'userid' : userid}))

    def __hidrate(self, raw_data):
        return [Rule(element['userid'], element['rule_text'], element['triggers']) for element in raw_data]