from .abstract.syntax_kind import SyntaxKind
from .binary_expression_syntax import BinaryExpressionSyntax
from .literal_expression_syntax import LiteralExpressionSyntax
from .parenthesized_expression_syntax import ParenthesizedExpressionSyntax
from .unary_expression_syntax import UnaryExpressionSyntax


class Evaluator:

    def __init__(self, root):
        self.__root = root

    def evaluate(self):
        return self.__evaluate_expression(self.__root)

    def __evaluate_expression(self, node):

        if type(node) == LiteralExpressionSyntax:
            return node.value

        if type(node) == UnaryExpressionSyntax:
            result = self.__evaluate_expression(node.operand)
            if node.operator_token.kind == SyntaxKind.PlusToken:
                return int(result)
            if node.operator_token.kind == SyntaxKind.MinusToken:
                return -int(result)
            raise Exception(
                f"Invalid Unary Operator Token {node.operator_token.kind.name}")

        if type(node) == BinaryExpressionSyntax:
            left = self.__evaluate_expression(node.left)
            right = self.__evaluate_expression(node.right)

            if node.operator_token.kind == SyntaxKind.PlusToken:
                return int(left) + int(right)
            if node.operator_token.kind == SyntaxKind.MinusToken:
                return int(left) - int(right)
            if node.operator_token.kind == SyntaxKind.StarToken:
                return int(left) * int(right)
            if node.operator_token.kind == SyntaxKind.SlashToken:
                return int(left) // int(right)
            raise Exception(
                f"Invalid Binary Operator Token {node.operator_token.kind.name}")

        if type(node) == ParenthesizedExpressionSyntax:
            return self.__evaluate_expression(node.expression)

        raise Exception(
            f"Invalid node kind {node.kind.name}")
