class Event:
    TYPE_SENSOR_RECEIVED = 'sensor_received'
    TYPE_SENSOR_PERSISTED = 'sensor_persisted'

    def __init__(self, name: str, model) -> None:
        self.name = name
        self.model = model