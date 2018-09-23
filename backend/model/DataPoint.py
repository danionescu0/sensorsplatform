import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model


class DataPoint:
    def __init__(self, sensor_id: str, timestamp: int, value):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value