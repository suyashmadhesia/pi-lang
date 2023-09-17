from .abstract.bound_expression import BoundExpression
from .abstract.bound_node_kind import BoundNodeKind
from .bound_binary_operator import BoundBinaryOperator


class BoundBinaryExpression(BoundExpression):

    def __init__(self, left: BoundExpression,
                 op: BoundBinaryOperator, right: BoundExpression) -> None: ...

    @property
    def left(self) -> BoundExpression: ...

    @property
    def op(self) -> BoundBinaryOperator: ...

    @property
    def right(self) -> BoundExpression: ...

    @property
    def kind(self) -> BoundNodeKind: ...
