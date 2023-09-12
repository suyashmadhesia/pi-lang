from syntax.generics.ie_enumerable import IEnumerable
from syntax.syntax_node import SyntaxNode
from .abstract.expression_syntax import ExpressionSyntax
from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable
from .syntax_node import SyntaxNode
from .syntax_token import SyntaxToken


class UnaryExpressionSyntax(ExpressionSyntax):

    def __init__(self, operator_token: SyntaxToken,
                 operand: ExpressionSyntax) -> None: ...

    @property
    def operator_token(self) -> SyntaxToken: ...

    @property
    def operand(self) -> ExpressionSyntax: ...

    @property
    def kind(self) -> SyntaxKind: ...

    def get_children(self) -> IEnumerable[SyntaxNode]: ...
