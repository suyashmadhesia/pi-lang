from .generics.ie_enumerable import IEnumerable
from .syntax_node import SyntaxNode
from .abstract.syntax_kind import SyntaxKind
from .syntax_token import SyntaxToken
from .abstract.expression_syntax import ExpressionSyntax


class BinaryExpressionSyntax(ExpressionSyntax):

    def __init__(self, left: ExpressionSyntax,
                 operator_token: SyntaxToken, right: ExpressionSyntax) -> None: ...

    @property
    def kind(self) -> SyntaxKind: ...

    @property
    def left(self) -> ExpressionSyntax: ...

    @property
    def operator_token(self) -> SyntaxToken: ...

    @property
    def right(self) -> ExpressionSyntax: ...

    def get_children(self) -> IEnumerable[SyntaxNode]: ...
