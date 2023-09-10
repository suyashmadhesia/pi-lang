from .abstract.syntax_kind import SyntaxKind
from .binary_expression_syntax import BinaryExpressionSyntax
from .literal_expression_syntax import LiteralExpressionSyntax


class Evaluator:

    def __init__(self, root):
        self.__root = root

    def evaluate(self):
        return self.__evaluate_expression(self.__root)

    def __evaluate_expression(self, node):

        if type(node) == LiteralExpressionSyntax:
            return node.value

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
                f"Invalid Operator Token {node.operator_token.kind.name}")
        raise Exception(
                f"Invalid node kind {node.kind}")