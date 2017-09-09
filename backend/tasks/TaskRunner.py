from typing import List

from model.Event import Event
from tasks.BaseTask import BaseTask


class TaskRunner():
    def __init__(self):
        self.__tasks = []

    def run(self, name: str, event: Event) -> None:
        running_list = filter(
            lambda task: task.get_name() == name and event.name == task.get_subscribed_event(),
            self.__tasks)
        for task in running_list:
            task.run(event)

    def add_task(self, task: BaseTask):
        self.__tasks.append(task)

    def get_event_name_from_task_name(self, name):
        tasks = filter(lambda task: task.get_name() == name, self.__tasks)

        return next(tasks).get_subscribed_event()

    def list_task_names(self) -> List[str]:
        return [task.get_name() for task in self.__tasks]