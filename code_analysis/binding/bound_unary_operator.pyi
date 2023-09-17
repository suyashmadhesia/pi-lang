from typing import List, TypeVar

from code_analysis.syntax.abstract.syntax_kind import SyntaxKind

from .abstract.bound_unary_operator_kind import BoundUnaryOperatorKind

T = TypeVar("T")

class BoundUnaryOperator:
    __operator: List["BoundUnaryOperator"]

    def __init__(
        self,
        syntax_kind: SyntaxKind,
        kind: BoundUnaryOperatorKind,
        operand_type: T,
        result_type: T | None,
    ) -> None: ...
    @property
    def syntax_kind(self) -> SyntaxKind: ...
    @property
    def operand_type(self) -> T: ...
    @property
    def result_type(self) -> T: ...
    @property
    def kind(self) -> BoundUnaryOperatorKind: ...
    @classmethod
    def initialize_operators(cls) -> None: ...
    @classmethod
    def bind(
        cls, kind: SyntaxKind, operator_type: T
    ) -> "BoundUnaryOperator" | None: ...
