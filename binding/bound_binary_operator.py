from syntax.abstract.syntax_kind import SyntaxKind
from binding.abstract.bound_binary_operator_kind import BoundBinaryOperatorKind


class BoundBinaryOperator:

    __operators = [
        'BoundBinaryOperator'(
            SyntaxKind.PlusToken, BoundBinaryOperatorKind.Addition, int),
        'BoundBinaryOperator'(
            SyntaxKind.MinusToken, BoundBinaryOperatorKind.Subtraction, int),
        'BoundBinaryOperator'(
            SyntaxKind.SlashToken, BoundBinaryOperatorKind.Division, int),
        'BoundBinaryOperator'(
            SyntaxKind.StarToken, BoundBinaryOperatorKind.Multiplication, int),
    ]

    def __init__(self, syntax_kind, kind, left_type, right_type, result_type=None):
        self.__syntax_kind = syntax_kind
        self.__kind = kind
        self.__left_type = left_type
        self.__right_type = right_type
        self.__result_type = result_type

    @property
    def kind(self):
        return self.__kind
    
    @property
    def syntax_kind(self):
        return self.__syntax_kind
    
    @property
    def left_type(self):
        return self.__left_type
    
    @property
    def right_type(self):
        return self.__right_type

    @property
    def result_type(self):
        return self.__result_type
    
    @classmethod
    def bind(cls, kind, left_type, right_type):
        for op in cls.__operators:
            if op.syntax_kind == kind and op.left_type == left_type and op.right_type == right_type:
                return op
        return None
