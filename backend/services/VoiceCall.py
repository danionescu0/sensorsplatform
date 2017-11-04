import abc


class VoiceCall(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def call(self, number: str, text: str) -> None:
        pass