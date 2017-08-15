from __future__ import absolute_import
from celery import Task
import time

class SendAlert(Task):
    ignore_result = True

    def run(self, event, *args, **kwargs):
        time.sleep(2)
        print("Event=" + event)
