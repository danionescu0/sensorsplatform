import time

from blinker import signal

from sync_events.ValidRuleEvent import ValidRuleEvent
from repository.AlertRepository import AlertRepository
from model.Alert import Alert


class AddAlertInHistoryListener:
    def __init__(self, alert_repository: AlertRepository) -> None:
        self.__alert_repository = alert_repository

        signal(ValidRuleEvent.NAME).connect(self.callback)

    def callback(self, valid_rule_event: ValidRuleEvent):
        rule = valid_rule_event.rule
        alert = Alert(None, rule.userid, rule.id, time.time())
        self.__alert_repository.create(alert)