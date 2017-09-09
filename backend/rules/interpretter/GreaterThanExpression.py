from rules.interpretter.OperatorExpression import OperatorExpression
from rules.interpretter.InterpretterContext import InterpretterContext

class GreaterThanExpression(OperatorExpression):
    def do_interpret(self, context: InterpretterContext, left_result, right_result) -> None:
        print(right_result)
        context.set(self, left_result > right_result)

    def __repr__(self):
        return 'Gt ({0}) and ({1})'.format(self.__left_operator, self.__right_operator)