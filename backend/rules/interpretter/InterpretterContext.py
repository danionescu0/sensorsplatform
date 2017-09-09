from rules.interpretter.Expression import Expression

class InterpretterContext:
    def __init__(self):
        self.__expressions = {}

    def set(self, expression: Expression, value):
        self.__expressions[expression.get_key()] = value

    def lookup(self, expression: Expression):
        return self.__expressions[expression.get_key()]