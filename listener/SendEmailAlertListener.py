from blinker import signal
from lock.RuleTimedLock import RuleTimedLock

from model.Rule import Rule
from services.EmailSender import EmailSender
from sync_events.ValidRuleEvent import ValidRuleEvent


class SendEmailAlertListener:
    CONTEXT = 'email'

    def __init__(self, email_sender: EmailSender, timed_lock: RuleTimedLock) -> None:
        self.__email_sender = email_sender
        self.__timed_lock = timed_lock

        signal(ValidRuleEvent.NAME).connect(self.callback)

    def callback(self, valid_rule_event: ValidRuleEvent):
        rule = valid_rule_event.rule
        if Rule.TRIGGER_EMAIL not in rule.triggers:
            print("skipping email not suppose to send")
            return
        if self.__timed_lock.has_lock(rule, self.CONTEXT):
            print("skipping email, lock")
            return False

        body = "An alert has been raised for rule: {0}".format(rule.rule_text)
        self.__email_sender.send("Email alert", body)
        self.__timed_lock.set_lock(rule, self.CONTEXT)