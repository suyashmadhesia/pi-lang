from typing import TypeVar

from .abstract.bound_expression import BoundExpression
from .abstract.bound_unary_operator_kind import BoundUnaryOperatorKind
from .bound_unary_operator import BoundUnaryOperator

T = TypeVar("T")

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
