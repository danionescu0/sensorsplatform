import argparse
import json

from repository.Sensors import Sensors
from tasks.SendEmailAlert import SendEmailAlert
from tasks.StoreData import StoreData
from tasks.TaskRunner import TaskRunner
import config

sensors_repo = Sensors(config.rabbitmq_host)
sensors_repo.connect()
task_runner = TaskRunner()
task_runner.add_task(SendEmailAlert(config.email['email'], config.email['password'], config.email['notifiedAddress']))
task_runner.add_task(StoreData())

parser = argparse.ArgumentParser(description='Tasks')
parser.add_argument('--task', dest='task', type=str)
parser.set_defaults(feature=False)
args = parser.parse_args()
print(args.task)

def receiver(ch, method, properties, body):
    print(" [x] Received %r" % body)
    task_runner.run(args.task, json.loads(body.decode()))

sensors_repo.consume(receiver)
