from logging import RootLogger

from tasks.BaseTask import BaseTask
from repository.UsersRepository import UsersRepository
from repository.RulesRepository import RulesRepository
from repository.SensorsRepository import SensorsRepository
from rules.RuleChecker import RuleChecker
from model.Event import Event
from sync_events.ValidRuleEvent import ValidRuleEvent


class RulesEvaluator(BaseTask):
    def __init__(self, rules_repository: RulesRepository,
                 sensors_repository: SensorsRepository,
                 users_repository: UsersRepository,
                 rule_checker: RuleChecker,
                 valid_rule_event: ValidRuleEvent,
                 logging: RootLogger) -> None:
        self.__rules_repository = rules_repository
        self.__sensors_repository = sensors_repository
        self.__users_repository = users_repository
        self.__rule_checker = rule_checker
        self.__valid_rule_event = valid_rule_event
        self.__logging = logging

    def run(self, event: Event):
        sensor = event.model
        user = self.__users_repository.get_by_sensor_id(sensor.id)
        if None == user:
            return
        rules = self.__rules_repository.get_for_user(user.userid)
        if 0 == len(rules):
            return
        for rule in rules:
            self.__logging.info("Checking rule: {0}".format(rule.rule_text))
            if self.__rule_checker.is_valid(rule):
                self.__valid_rule_event.send(rule)
                self.__logging.info("Rule is valid")

    def get_name(self):
        return 'rules_evaluator'

    def get_subscribed_event(self):
        return Event.TYPE_SENSOR_PERSISTED