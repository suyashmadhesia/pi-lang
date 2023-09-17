from .abstract.expression_syntax import ExpressionSyntax
from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable
from .syntax_token import SyntaxToken
from .syntax_tree import SyntaxTree

class Parser:
    def __init__(self, text: str) -> None: ...
    @property
    def diagnostics(self) -> IEnumerable[str]: ...
    def __next_token(self) -> SyntaxToken: ...
    def __match_token(self, kind: SyntaxKind) -> SyntaxToken: ...
    def __peek(self, offset: int) -> SyntaxToken: ...
    @property
    def current(self) -> SyntaxToken: ...
    def parse(self) -> SyntaxTree: ...
    def __parse_expression(self, parent_precedence: int) -> ExpressionSyntax: ...
    def __parse_primary_expression(self) -> ExpressionSyntax: ...