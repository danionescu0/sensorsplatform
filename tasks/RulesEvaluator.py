from tasks.BaseTask import BaseTask
from repository.UsersRepository import UsersRepository
from repository.RulesRepository import RulesRepository
from rules.RuleChecker import RuleChecker
from repository.SensorsRepository import SensorsRepository
from model.Event import Event
from model.Sensor import Sensor

class RulesEvaluator(BaseTask):
    def __init__(self, rules_repository: RulesRepository,
                 sensors_repository: SensorsRepository,
                 users_repository: UsersRepository,
                 rule_checker: RuleChecker) -> None:
        self.__rules_repository = rules_repository
        self.__sensors_repository = sensors_repository
        self.__users_repository = users_repository
        self.__rule_checker = rule_checker

    def run(self, event: Event):
        if event.name == 'sensor':
            self.__process_event(event.model)

    def __process_event(self, sensor: Sensor):
        user = self.__users_repository.get_by_sensor_id(sensor.id)
        if None == user:
            return
        rules = self.__rules_repository.get_for_user(user.userid)
        if None == rules:
            return
        print(rules)
        for rule in rules:
            print("Checking rule:" + rule.rule_text)
            if self.__rule_checker.is_valid(rule):
                print('rule: is valid')
            else:
                print('rule is not valid')

    def get_name(self):
        return 'rules_evaluator'