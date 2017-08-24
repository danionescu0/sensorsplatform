class TaskRunner():
    def __init__(self):
        self.__tasks = []

    def run(self, name: str, data: str):
        running_list = filter(lambda task: task.get_name() == name, self.__tasks)
        for task in running_list:
            task.run(data)

    def add_task(self, task):
        self.__tasks.append(task)

    def list_task_names(self):
        return [task.get_name() for task in self.__tasks]