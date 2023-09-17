from .abstract.expression_syntax import ExpressionSyntax
from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable
from .syntax_node import SyntaxNode


class UnaryExpressionSyntax(ExpressionSyntax):

    def __init__(self, operator_token, operand):
        self.__operatorToken = operator_token
        self.__operand = operand

    @property
    def operator_token(self):
        return self.__operatorToken

    @property
    def operand(self):
        return self.__operand

    @property
    def kind(self):
        return SyntaxKind.UnaryExpression

    def get_children(self) -> IEnumerable[SyntaxNode]:
        return IEnumerable([self.operator_token, self.operand])
