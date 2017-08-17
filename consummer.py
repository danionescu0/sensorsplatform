import argparse
import json

from repository.AsyncJobs import AsyncJobs
from tasks.SendEmailAlert import SendEmailAlert
from tasks.StoreData import StoreData
from tasks.TaskRunner import TaskRunner
from repository.RulesRepository import RulesRepository
from repository.SensorsRepository import SensorsRepository
from rules.parser.ExpressionBuilder import ExpressionBuilder
from rules.parser.Tokenizer import Tokenizer
from rules.interpretter.InterpretterContext import InterpretterContext
from rules.parser.ParseException import ParseException
import config

sensors_repo = AsyncJobs(config.rabbitmq_host)
sensors_repo.connect()
task_runner = TaskRunner()
task_runner.add_task(SendEmailAlert(config.email['email'], config.email['password'], config.email['notifiedAddress']))
task_runner.add_task(StoreData())

rules_repository = RulesRepository(config.mongodb_uri)

parser = argparse.ArgumentParser(description='Tasks')
parser.add_argument('--task', dest='task', type=str)
parser.set_defaults(feature=False)
args = parser.parse_args()
print(args.task)

def receiver(ch, method, properties, body):
    print(" [x] Received %r" % body)
    task_runner.run(args.task, json.loads(body.decode()))

sensors_repo.consume(receiver)
