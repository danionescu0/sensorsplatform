from rules.parser.ParseException import ParseException
from rules.interpretter.EqualsExpression import EqualsExpression
from rules.interpretter.BooleanOrExpression import BooleanOrExpression
from rules.interpretter.BooleanAndExpression import BooleanAndExpression
from rules.interpretter.LiteralExpression import LiteralExpression
from rules.interpretter.GreaterThanExpression import GreaterThanExpression
from rules.interpretter.LessThanExpression import LessThanExpression
from rules.interpretter.BetweenExpression import BetweenExpression
from rules.parser.Token import Token
from rules.parser.Tokenizer import Tokenizer
from rules.interpretter.Expression import Expression

class ExpressionBuilder:
    current_token_index = 0

    def __init__(self, tokenizer: Tokenizer):
        self.__tokenizer = tokenizer
        self.__current_token_index = 0

    def set_text(self, text: str) -> None:
        self.__text = text
        self.__expression = None

    def build(self):
        ExpressionBuilder.current_token_index = 0
        self.__tokens = self.__tokenizer.tokenize(self.__text)
        self.__expression = self.__evaluate()

    def get_expression(self) -> Expression:
        return self.__expression

    def __evaluate(self):
        token = self.__get_current_token()
        token_type = token.get_type()
        self.__next_token()
        if token_type in [Token.TYPE_LITERAL_BOOLEAN, Token.TYPE_LITERAL_INT, Token.TYPE_LITERAL_TIME, Token.TYPE_ACTUATOR_STATE]:
            return LiteralExpression(token.get_value())
        elif token_type == Token.TYPE_CURRENT_TIME or token_type == Token.TYPE_SENSOR:
            return LiteralExpression(token.get_value())

        left_expr = self.__evaluate()
        right_expr = self.__evaluate()
        if token_type == Token.TYPE_EXPR_BETWEEN:
            third_expr = self.__evaluate()
            return BetweenExpression(left_expr, right_expr, third_expr)
        if token_type == Token.TYPE_EXPR_EQUAL:
            return EqualsExpression(left_expr, right_expr)
        elif token_type == Token.TYPE_BOOLEAN_AND:
            return BooleanAndExpression(left_expr, right_expr)
        elif token_type == Token.TYPE_BOOLEAN_OR:
            return BooleanOrExpression(left_expr, right_expr)
        elif token_type == Token.TYPE_EXPR_GREATER:
            return GreaterThanExpression(left_expr, right_expr)
        elif token_type == Token.TYPE_EXPR_LESS:
            return LessThanExpression(left_expr, right_expr)

        raise ParseException("Token type {0} not implemented".format(token_type))

    def __get_current_token(self):
        return self.__tokens[ExpressionBuilder.current_token_index]

    def __next_token(self):
        ExpressionBuilder.current_token_index += 1