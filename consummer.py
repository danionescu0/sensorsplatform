import argparse
import pickle

from container import Container

parser = argparse.ArgumentParser(description='Tasks')
parser.add_argument('--task', dest='task', type=str)
parser.set_defaults(feature=False)
args = parser.parse_args()

container = Container()
async_jobs = container.get('async_jobs')
async_jobs.connect()
task_runner = container.get('task_runner')
send_email_alert_listener = container.get('send_email_alert_listener')


def callback(ch, method, properties, body):
    event = pickle.loads(body)
    task_runner.run(args.task, event)

async_jobs.consume(callback)