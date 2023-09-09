from typing import TypeVar

from .generics.ie_enumerable import IEnumerable
from .syntax_token import SyntaxToken

T = TypeVar("T")


class Lexer:

    def __init__(self, text: str) -> None: ...

    def __peek(self, offset: int) -> chr: ...

    def lex(self) -> SyntaxToken: ...

    def next(self) -> None: ...

    @property
    def diagnostics(self) -> IEnumerable[T]: ...

    @property
    def current(self) -> chr: ...
