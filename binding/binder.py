from typing import List
from syntax.abstract.syntax_kind import SyntaxKind

from syntax.generics.ie_enumerable import IEnumerable


class Binder:

    def __init__(self, syntax):
        self.__syntax = syntax
        self.__diagnostics: List[str] = []

    @property
    def diagnostics(self):
        return IEnumerable(self.__diagnostics)

    def bind_expression(self, syntax):
        if syntax.kind == SyntaxKind.LiteralExpression:
            return self.__bind_literal_expression(syntax)
        if syntax.kind == SyntaxKind.BinaryExpression:
            return self.__bind_binary_expression(syntax)
        if syntax.kind == SyntaxKind.UnaryExpression:
            return self.__bind_unary_expression(syntax)
        if syntax.kind == SyntaxKind.ParenthesizedExpression:
            return self.bind_expression(syntax.expression)
        raise Exception(f'Unexpected syntax {syntax.kind}')

    def __bind_unary_expression(self, syntax): ...

    def __bind_binary_expression(self, syntax): ...

    def __bind_literal_expression(self, syntax):
        value = syntax.value if syntax.value else 0
        ...
