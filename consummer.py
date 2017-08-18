import argparse
import json

from container import Container

container = Container()

parser = argparse.ArgumentParser(description='Tasks')
parser.add_argument('--task', dest='task', type=str)
parser.set_defaults(feature=False)
args = parser.parse_args()
async_jobs = container.get('async_jobs')
async_jobs.connect()
task_runner = container.get('task_runner')


def receiver(ch, method, properties, body):
    print(" [x] Received %r" % body)
    task_runner.run(args.task, json.loads(body.decode()))

async_jobs.consume(receiver)
