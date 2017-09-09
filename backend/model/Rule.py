from typing import List

class Rule():
    TRIGGER_EMAIL = 'email'
    TRIGGER_SMS = 'sms'
    trigger_min_interval = 0

    def __init__(self, userid: str, rule_text: str, triggers: List[str]) -> None:
        self.userid = userid
        self.rule_text = rule_text
        self.triggers = triggers

    def get_id(self):
        return self.userid + self.rule_text