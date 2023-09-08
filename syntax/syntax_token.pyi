from typing import TypeVar

from .generics.ie_enumerable import IEnumerable
from .syntax_node import SyntaxNode
from .abstract.syntax_kind import SyntaxKind

T = TypeVar('T')


class SyntaxToken(SyntaxNode):

    def __init__(self, kind: SyntaxKind, position: int,
                 text: str, value: T = None) -> None: ...

    @property
    def kind(self) -> SyntaxKind: ...

    @property
    def position(self) -> int: ...

    @property
    def text(self) -> str: ...

    @property
    def value(self) -> T: ...

    def get_children(self) -> IEnumerable[SyntaxNode]: ...
