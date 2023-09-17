from code_analysis.binding.abstract.bound_binary_operator_kind import BoundBinaryOperatorKind
from code_analysis.binding.abstract.bound_unary_operator_kind import BoundUnaryOperatorKind
from code_analysis.binding.bound_binary_expression import BoundBinaryExpression
from code_analysis.binding.bound_literal_expression import BoundLiteralExpression
from code_analysis.binding.bound_unary_expression import BoundUnaryExpression


class Evaluator:

    def __init__(self, root):
        self.__root = root

    def evaluate(self):
        return self.__evaluate_expression(self.__root)

    def __evaluate_expression(self, node):
        if type(node) == BoundLiteralExpression:
            return node.value

        if type(node) == BoundUnaryExpression:
            result = self.__evaluate_expression(node.operand)
            if node.op.kind == BoundUnaryOperatorKind.Identity:
                return int(result)
            if node.op.kind == BoundUnaryOperatorKind.Negation:
                return -int(result)
            raise Exception(
                f"Invalid Unary Operator Token {node.op.kind.name}")

        if type(node) == BoundBinaryExpression:
            left = self.__evaluate_expression(node.left)
            right = self.__evaluate_expression(node.right)

            if node.op.kind == BoundBinaryOperatorKind.Addition:
                return int(left) + int(right)
            if node.op.kind == BoundBinaryOperatorKind.Subtraction:
                return int(left) - int(right)
            if node.op.kind == BoundBinaryOperatorKind.Multiplication:
                return int(left) * int(right)
            if node.op.kind == BoundBinaryOperatorKind.Division:
                return int(left) // int(right)
            raise Exception(
                f"Invalid Binary Operator Token {node.op.kind.name}")
        raise Exception(
            f"Invalid node kind {node.kind.name}")
