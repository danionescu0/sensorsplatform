from rules.parser.ExpressionBuilder import ExpressionBuilder
from rules.interpretter.InterpretterContext import InterpretterContext
from rules.parser.ParseException import ParseException
from model.Rule import Rule
from services.TimedLock import TimedLock

class RuleChecker:
    def __init__(self, expression_builder: ExpressionBuilder, interpretter_context: InterpretterContext,
                 timed_lock: TimedLock) -> None:
        self.__expression_builder = expression_builder
        self.__interpretter_context = interpretter_context
        self.__timed_lock = timed_lock

    def is_valid(self, rule: Rule):
        if self.__timed_lock.has_lock(rule.get_id()):
            return False
        self.__expression_builder.set_text(rule.rule_text)
        try:
            self.__expression_builder.build()
        except ParseException as e:
            return False
        statement = self.__expression_builder.get_expression()
        statement.interpret(self.__interpretter_context)

        return self.__interpretter_context.lookup(statement)