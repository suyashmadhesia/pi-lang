from .abstract.expression_syntax import ExpressionSyntax
from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable
from .syntax_node import SyntaxNode
from .syntax_token import SyntaxToken

class LiteralExpressionSyntax(ExpressionSyntax):

    def __init__(self,
                 literal_token: SyntaxToken, value: any) -> None: ...

    @property
    def kind(self) -> SyntaxKind: ...

    @property
    def value(self) -> any: ...

    @property
    def literal_token(self) -> SyntaxToken: ...

    def get_children(self) -> IEnumerable[SyntaxNode]: ...
