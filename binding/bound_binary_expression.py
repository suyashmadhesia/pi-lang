from binding.abstract.bound_expression import BoundExpression
from binding.abstract.bound_node_kind import BoundNodeKind


class BoundBinaryExpression(BoundExpression):

    def __init__(self, left, op, right):
        self.__left = left
        self.__op = op
        self.__right = right

    def left(self): return self.__left

    def right(self): return self.__right

    def op(self): return self.__op

    def kind(self): return BoundNodeKind.BinaryExpression

    def type(self): return self.op.type
