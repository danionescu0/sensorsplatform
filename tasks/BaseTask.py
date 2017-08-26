import abc

from model.Event import Event


class BaseTask(metaclass=abc.ABCMeta):
    def run(self, event: Event) -> None:
        pass

    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_subscribed_event(self) -> str:
        pass