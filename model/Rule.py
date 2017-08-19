from typing import List

class Rule():
    def __init__(self, userid: str, rule_text: str, triggers: List[str]) -> None:
        self.userid = userid
        self.rule_text = rule_text
        self.triggers = triggers