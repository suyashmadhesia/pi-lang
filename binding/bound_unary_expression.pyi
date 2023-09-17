from binding.abstract.bound_expression import BoundExpression
from binding.abstract.bound_unary_operator_kind import BoundUnaryOperatorKind
from binding.bound_unary_operator import BoundUnaryOperator
from typing import TypeVar

T = TypeVar('T')


class BoundUnaryExpression(BoundExpression):


    def __init__(self, op: BoundUnaryOperator, operand: BoundExpression) -> None: ...

    @property
    def operand(self) -> BoundExpression: ...

    @property
    def op(self) -> BoundUnaryExpression: ...

    @property
    def kind(self) -> BoundUnaryOperatorKind: ...

    @property
    def type(self) -> T: ...
