from typing import List

class Rule():
    TRIGGER_EMAIL = 'email'
    TRIGGER_SMS = 'sms'
    trigger_min_interval = 0

    def __init__(self, userid: str, rule_name: str, name: str, triggers: List[str]) -> None:
        self.userid = userid
        self.name = rule_name
        self.rule_text = name
        self.triggers = triggers

    def get_id(self):
        return self.userid + self.rule_text