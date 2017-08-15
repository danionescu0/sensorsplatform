from repository.Sensors import Sensors
from tasks.SendAlert import SendAlert
import config

sensors_repo = Sensors(config.rabbitmq_host)
sensors_repo.connect()

def receiver(ch, method, properties, body):
    print(" [x] Received %r" % body)

sensors_repo.consume(receiver)
