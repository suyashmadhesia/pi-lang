from .abstract.bound_expression import BoundExpression
from .abstract.bound_node_kind import BoundNodeKind


class BoundLiteralExpression(BoundExpression):
    def __init__(self, value):
        self.__value = value

    @property
    def kind(self):
        return BoundNodeKind.LiteralExpression

    @property
    def type(self):
        return type(self.__value)

    @property
    def value(self):
        return self.__value
