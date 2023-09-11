from .generics.ie_enumerable import IEnumerable
from .syntax_node import SyntaxNode
from .abstract.syntax_kind import SyntaxKind
from .abstract.expression_syntax import ExpressionSyntax


class UnaryExpressionSyntax(ExpressionSyntax):

    def __init__(self, operatorToken, operand):
        self.__operatorToken = operatorToken
        self.__operand = operand

    @property
    def operatorToken(self):
        return self.__operatorToken

    @property
    def operand(self):
        return self.__operand

    @property
    def kind(self):
        return SyntaxKind.UnaryExpression

    def get_children(self) -> IEnumerable[SyntaxNode]:
        return IEnumerable([self.operatorToken, self.operand])
