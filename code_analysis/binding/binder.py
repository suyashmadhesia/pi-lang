from typing import List

from code_analysis.syntax.abstract.syntax_kind import SyntaxKind
from code_analysis.syntax.generics.ie_enumerable import IEnumerable

from .bound_binary_expression import BoundBinaryExpression
from .bound_binary_operator import BoundBinaryOperator
from .bound_literal_expression import BoundLiteralExpression
from .bound_unary_expression import BoundUnaryExpression
from .bound_unary_operator import BoundUnaryOperator


class Binder:
    def __init__(self):
        self.__diagnostics: List[str] = []
        BoundUnaryOperator.initialize_operators()
        BoundBinaryOperator.initialize_operators()

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
        raise Exception(f"Unexpected syntax {syntax.kind}")

    def __bind_unary_expression(self, syntax):
        bound_operand = self.bind_expression(syntax.operand)
        bound_operator = BoundUnaryOperator.bind(
            syntax.operator_token.kind, bound_operand.type
        )
        if bound_operator == None:
            self.__diagnostics.append(
                f"Unary operator {syntax.operator_token.text} is not defined for type {bound_operand.type}."
            )
            return bound_operand
        return BoundUnaryExpression(bound_operator, bound_operand)

    def __bind_binary_expression(self, syntax):
        bound_left = self.bind_expression(syntax.left)
        bound_right = self.bind_expression(syntax.right)
        bound_operator = BoundBinaryOperator.bind(
            syntax.operator_token.kind, bound_left.type, bound_right.type
        )
        if bound_operator == None:
            self.__diagnostics.append(
                f"Binary operator {syntax.operator_token.text} is not defined for type {bound_operator.type}."
            )
            return bound_left
        return BoundBinaryExpression(bound_left, bound_operator, bound_right)

    def __bind_literal_expression(self, syntax):
        value = syntax.value if syntax.value else 0
        return BoundLiteralExpression(value)
