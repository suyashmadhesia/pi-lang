from .abstract.bound_expression import BoundExpression
from .abstract.bound_node_kind import BoundNodeKind


class BoundBinaryExpression(BoundExpression):
    def __init__(self, left, op, right):
        self.__left = left
        self.__op = op
        self.__right = right

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def op(self):
        return self.__op

    @property
    def kind(self):
        return BoundNodeKind.BinaryExpression

    @property
    def type(self):
        return self.op.type
