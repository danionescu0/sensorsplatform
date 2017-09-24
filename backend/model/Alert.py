class Alert:
    def __init__(self, id: str, userid: str, rule_id: str, timestamp: int) -> None:
        self.id = id
        self.userid = userid
        self.rule_id = rule_id
        self.timestamp = timestamp