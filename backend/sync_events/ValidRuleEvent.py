from blinker import signal

from model.Rule import Rule


class ValidRuleEvent:
    NAME = 'valid_rule_event'

    def send(self, rule: Rule):
        event = signal(self.NAME)
        self.rule = rule
        event.send(self)