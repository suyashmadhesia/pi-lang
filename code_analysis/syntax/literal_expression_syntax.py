from .abstract.expression_syntax import ExpressionSyntax
from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable


class LiteralExpressionSyntax(ExpressionSyntax):

    def __init__(self, literal_token, value=None):
        self.__literal_token = literal_token
        self.__value = value

    
    @property
    def literal_token(self):
        return self.__literal_token
    
    @property
    def value(self):
        return self.__value if self.__value is not None else self.literal_token.value
    
    @property
    def kind(self):
        return SyntaxKind.LiteralExpression
    

    def get_children(self):
        return IEnumerable([self.__literal_token])