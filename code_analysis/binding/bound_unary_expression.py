from .abstract.bound_expression import BoundExpression


class BoundUnaryExpression(BoundExpression):

    def __init__(self, op, operand):
        self.__op = op
        self.__operand = operand

    @property
    def operand(self):
        return self.__operand

    @property
    def op(self):
        return self.__op

    @property
    def kind(self):
        return self.op.kind

    @property
    def type(self):
        return self.op.type