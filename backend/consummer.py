import time
import argparse
import pickle
import sys

from container import Container


parser = argparse.ArgumentParser(description='Tasks')
parser.add_argument('--task', dest='task', type=str)
parser.add_argument('--list', dest='list', action='store_true', default=False)
args = parser.parse_args()

container = Container()

time.sleep(5)
async_jobs = container.async_jobs()
task_runner = container.task_runner()

if args.list:
    print("Available tasks:")
    print(task_runner.list_task_names())
    sys.exit()

event_name = task_runner.get_event_name_from_task_name(args.task)
send_email_alert_listener = container.send_email_alert_listener()
voice_alert_listener = container.telestax_voice_call()
add_alerts_in_history_listener = container.add_alert_in_history_listener()
async_jobs.register_event(event_name)

def callback(ch, method, properties, body):
    event = pickle.loads(body)
    task_runner.run(args.task, event)

async_jobs.consume(callback)