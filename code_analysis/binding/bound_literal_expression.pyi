from typing import TypeVar

from .abstract.bound_expression import BoundExpression
from .abstract.bound_node_kind import BoundNodeKind

T = TypeVar("T")

class BoundLiteralExpression(BoundExpression):
    def __init__(self, value: T) -> None: ...
    @property
    def kind(self) -> BoundNodeKind: ...
    @property
    def type(self) -> T: ...
    @property
    def value(self) -> T: ...
