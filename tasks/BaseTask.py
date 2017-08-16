import abc

class BaseTask(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_name(self):
        pass