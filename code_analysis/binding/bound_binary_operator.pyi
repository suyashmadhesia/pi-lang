from typing import List, TypeVar

from code_analysis.syntax.abstract.syntax_kind import SyntaxKind

from .abstract.bound_binary_operator_kind import BoundBinaryOperatorKind

T = TypeVar("T")

class BoundBinaryOperator:
    __operators: List["BoundBinaryOperator"]

    def __init__(
        self,
        syntax_kind: SyntaxKind,
        kind: BoundBinaryOperatorKind,
        left_type: T,
        right_type: T,
        type: T | None,
    ) -> None: ...
    @property
    def syntax_kind(self) -> SyntaxKind: ...
    @property
    def left_type(self) -> T: ...
    @property
    def right_type(self) -> T: ...
    @property
    def result_type(self) -> T: ...
    @property
    def kind(self) -> BoundBinaryOperatorKind: ...
    @classmethod
    def initialize_operators(cls) -> None: ...
    @classmethod
    def bind(
        cls, kind: SyntaxKind, left_type: T, right_type: T
    ) -> "BoundBinaryOperator" | None: ...
