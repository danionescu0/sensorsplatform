from lock.TimedLock import TimedLock
from model.Rule import Rule

class RuleTimedLock:
    RULE_LOCK_KEY = 'RULE_LOCK_{0}'

    def __init__(self, time_lock: TimedLock) -> None:
        self.__timed_lock = time_lock

    def set_lock(self, rule: Rule, context: str):
        self.__timed_lock.set_lock(self.__get_lock_key(rule, context), int(rule.trigger_min_interval))

    def has_lock(self, rule: Rule, context: str):
        return self.__timed_lock.has_lock(self.__get_lock_key(rule, context))

    def __get_lock_key(self, rule: Rule, context: str):
        return self.RULE_LOCK_KEY.format(rule.get_id(), context)