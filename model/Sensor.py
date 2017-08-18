class Sensor():
    def __init__(self, id: int, type: str, latest_value: float) -> None:
        self.id = id
        self.type = type
        self.latest_value = latest_value