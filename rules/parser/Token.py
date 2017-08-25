class Token:
    TYPE_BOOLEAN_AND = 'and'
    TYPE_BOOLEAN_OR = 'or'
    TYPE_EXPR_EQUAL = 'eq'
    TYPE_EXPR_GREATER = 'gt'
    TYPE_EXPR_BETWEEN = 'btw'
    TYPE_EXPR_LESS = 'lt'
    TYPE_LITERAL_BOOLEAN = 'literal_bool'
    TYPE_ACTUATOR_STATE = 'actuator_state'
    TYPE_LITERAL_INT = 'literal_int'
    TYPE_LITERAL_TIME = 'literal_time'
    TYPE_CURRENT_TIME = 'time'
    TYPE_SENSOR = 'sensor'
    TYPE_AVERAGE_SENSOR = 'average_sensor'

    def __init__(self, type: str, value):
        self.__type = type
        self.__value = value

    def get_type(self) -> str:
        return self.__type

    def get_value(self):
        return self.__value