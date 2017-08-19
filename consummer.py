import argparse
import pickle

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
    event = pickle.loads(body)
    task_runner.run(args.task, event)

async_jobs.consume(receiver)
