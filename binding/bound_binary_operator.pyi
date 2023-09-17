from binding.abstract.bound_binary_operator_kind import BoundBinaryOperatorKind
from syntax.abstract.syntax_kind import SyntaxKind
from typing import TypeVar, List

T = TypeVar('T')


class BoundBinaryOperator:

    __operators = List['BoundBinaryOperator']

    def __init__(self, syntax_kind: SyntaxKind, kind: BoundBinaryOperatorKind,
                 left_type: T, right_type: T, result_type: T | None) -> None: ...

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
    def bind(cls, kind: SyntaxKind, left_type: T,
             right_type: T) -> 'BoundBinaryOperator' | None: ...
