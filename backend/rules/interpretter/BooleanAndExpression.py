from rules.interpretter.OperatorExpression import OperatorExpression
from rules.interpretter.InterpretterContext import InterpretterContext


class BooleanAndExpression(OperatorExpression):
    def do_interpret(self, context: InterpretterContext, left_result, right_result) -> None:
        context.set(self, left_result and right_result)

    def __repr__(self):
        return 'And ({0}) and ({1})'.format(self.__left_operator, self.__right_operator)