from rules.parser.ExpressionBuilder import ExpressionBuilder
from rules.interpretter.InterpretterContext import InterpretterContext
from rules.parser.ParseException import ParseException
from model.Rule import Rule

class RuleChecker:
    def __init__(self, expression_builder: ExpressionBuilder, interpretter_context: InterpretterContext) -> None:
        self.__expression_builder = expression_builder
        self.__interpretter_context = interpretter_context

    def is_valid(self, rule: Rule):
        self.__expression_builder.set_text(rule.rule_text)
        try:
            self.__expression_builder.build()
        except ParseException as e:
            print(e)
            return False
        statement = self.__expression_builder.get_expression()
        statement.interpret(self.__interpretter_context)

        return self.__interpretter_context.lookup(statement)