from .abstract.expression_syntax import ExpressionSyntax
from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable


class ParenthesizedExpressionSyntax(ExpressionSyntax):

    def __init__(self, open_parenthesis,
                 expression, close_parenthesis):
        self.__open_parenthesis = open_parenthesis
        self.__expression = expression
        self.__close_parenthesis = close_parenthesis

    @property
    def open_parenthesis(self):
        return self.__open_parenthesis

    @property
    def expression(self):
        return self.__expression

    @property
    def close_parenthesis(self):
        return self.__close_parenthesis

    @property
    def kind(self):
        return SyntaxKind.ParenthesizedExpression

    def get_children(self):
        return IEnumerable([self.open_parenthesis, self.expression, self.close_parenthesis])
