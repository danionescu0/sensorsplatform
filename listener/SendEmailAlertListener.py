from blinker import signal

from services.EmailSender import EmailSender
from sync_events.ValidRuleEvent import ValidRuleEvent
from model.Rule import Rule

class SendEmailAlertListener:
    def __init__(self, email_sender: EmailSender) -> None:
        self.__email_sender = email_sender
        signal(ValidRuleEvent.NAME).connect(self.callback)

    def callback(self, valid_rule_event: ValidRuleEvent):
        rule = valid_rule_event.rule
        if Rule.TRIGGER_SMS not in rule.triggers:
            print("skipping email")
            return

        body = "An alert has been raised for rule: {0}".format(rule.rule_text)
        self.__email_sender.send("Email alert", body)
        print ("Sending email alert!")