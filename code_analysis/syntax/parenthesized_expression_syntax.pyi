from .abstract.expression_syntax import ExpressionSyntax
from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable
from .syntax_node import SyntaxNode
from .syntax_token import SyntaxToken


class ParenthesizedExpressionSyntax(ExpressionSyntax):

    def __init__(self, open_parenthesis: SyntaxToken,
                 expression: ExpressionSyntax, close_parenthesis: SyntaxToken) -> None: ...


    @property
    def kind(self) -> SyntaxKind: ...

    @property
    def open_parenthesis(self) -> SyntaxToken:...

    @property
    def expression(self) -> ExpressionSyntax:...

    @property
    def close_parenthesis(self) -> SyntaxToken:...

    def get_children(self) -> IEnumerable[SyntaxNode]: ...