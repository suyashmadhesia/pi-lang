from binding.abstract.bound_unary_operator_kind import BoundUnaryOperatorKind
from syntax.abstract.syntax_kind import SyntaxKind
from typing import TypeVar, List

T = TypeVar('T')


class BoundUnaryOperator:

    __operator: List['BoundUnaryOperator']

    def __init__(self, syntax_kind: SyntaxKind,
                 kind: BoundUnaryOperatorKind, operand_type: T, result_type: T | None) -> None: ...

    @property
    def syntax_kind(self) -> SyntaxKind: ...

    @property
    def operand_type(self) -> T: ...

    @property
    def result_type(self) -> T: ...

    @property
    def kind(self) -> BoundUnaryOperatorKind: ...

    @classmethod
    def bind(cls, kind: SyntaxKind,
             operator_type: T) -> 'BoundUnaryOperator' | None: ...
