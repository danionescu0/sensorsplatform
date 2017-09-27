import json

from model.Rule import Rule
from repository.RulesRepository import RulesRepository
from security.secure import secure
from web.CorsHandler import CorsHandler


class RulesHandler(CorsHandler):
    def initialize(self, rules_repo: RulesRepository):
        self.__rules_repo = rules_repo

    @secure
    def get(self, user_id):
        rules = [rule.__dict__ for rule in self.__rules_repo.get_for_user(user_id)]
        self.write(json.dumps(rules))

    @secure
    def post(self, user_id):
        data = json.loads(self.request.body.decode("utf-8"))
        rule = Rule(None, user_id, data['rule_name'], data['rule_text'], data['triggers'])
        self.__rules_repo.create(rule)
        self.set_status(201)
