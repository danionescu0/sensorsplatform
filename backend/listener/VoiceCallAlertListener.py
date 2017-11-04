from logging import RootLogger

from blinker import signal
from lock.RuleTimedLock import RuleTimedLock

from model.Rule import Rule
from repository.UsersRepository import UsersRepository
from sync_events.ValidRuleEvent import ValidRuleEvent
from services.VoiceCall import VoiceCall


# todo merge with email alert listener to remove duplication
class VoiceCallAlertListener:
    CONTEXT = 'voice'

    def __init__(self, voice_call: VoiceCall, timed_lock: RuleTimedLock, users_repo: UsersRepository,
                 logging: RootLogger) -> None:
        self.__voice_call = voice_call
        self.__timed_lock = timed_lock
        self.__users_repo = users_repo
        self.__logging = logging
        signal(ValidRuleEvent.NAME).connect(self.callback)

    def callback(self, valid_rule_event: ValidRuleEvent):
        self.__logging.info('Checking voice call event')

        rule = valid_rule_event.rule
        if Rule.TRIGGER_VOICE_CALL not in rule.triggers:
            return
        if self.__timed_lock.has_lock(rule, self.CONTEXT):
            self.__logging.info("Skipping voice alert, lock found for rule: {0}".format(rule.rule_text))
            return False

        user = self.__users_repo.get_by_id(valid_rule_event.rule.userid)
        body = "An alert has been raised for rule: {0}".format(rule.rule_text)
        self.__logging.info(body)
        self.__voice_call.call(user.phone, body)
        self.__timed_lock.set_lock(rule, self.CONTEXT)