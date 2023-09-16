from binding.abstract.bound_expression import BoundExpression
from typing import TypeVar

from binding.abstract.bound_node_kind import BoundNodeKind

T = TypeVar('T')


class BoundLiteralExpression(BoundExpression):

    def __init__(self, object: T) -> None: ...

    @property
    def kind(self) -> BoundNodeKind: ...

    @property
    def type(self) -> T: ...