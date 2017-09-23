class Alert:
    def __init__(self, id: str, timestamp: int, rule_id: str) -> None:
        self.id = id
        self.timestamp = timestamp
        self.rule_id = rule_id