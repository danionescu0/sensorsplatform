import abc

class TokenConverter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_value(self, token_raw_value: str):
        pass

    @abc.abstractmethod
    def supports(self, token_type: str):
        pass