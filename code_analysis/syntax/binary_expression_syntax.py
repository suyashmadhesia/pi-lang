from .abstract.expression_syntax import ExpressionSyntax
from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable


class BinaryExpressionSyntax(ExpressionSyntax):

    def __init__(self, left, operator_token, right):
        self.__left = left
        self.__operator_token = operator_token
        self.__right = right

    @property
    def left(self):
        return self.__left
    
    @property
    def operator_token(self):
        return self.__operator_token

    @property
    def right(self):
        return self.__right
    
    @property
    def kind(self):
        return SyntaxKind.BinaryExpression
    

    def get_children(self):
        return IEnumerable([self.__left, self.__operator_token, self.__right])
        