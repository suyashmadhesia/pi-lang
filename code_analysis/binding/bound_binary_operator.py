from code_analysis.syntax.abstract.syntax_kind import SyntaxKind

from .abstract.bound_binary_operator_kind import BoundBinaryOperatorKind


class BoundBinaryOperator:
    __operators = []

    def __init__(self, syntax_kind, kind, left_type, right_type=None, type=None):
        self.__syntax_kind = syntax_kind
        self.__kind = kind
        self.__left_type = left_type
        self.__right_type = left_type if right_type is None else right_type
        self.__type = left_type if type is None else type

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
    def type(self):
        return self.__type

    @classmethod
    def initialize_operators(cls):
        cls.__operators = [
            cls(SyntaxKind.PlusToken, BoundBinaryOperatorKind.Addition, int),
            cls(SyntaxKind.MinusToken, BoundBinaryOperatorKind.Subtraction, int),
            cls(SyntaxKind.SlashToken, BoundBinaryOperatorKind.Division, int),
            cls(SyntaxKind.StarToken, BoundBinaryOperatorKind.Multiplication, int),
            cls(
                SyntaxKind.EqualEqualToken,
                BoundBinaryOperatorKind.Equals,
                int,
                type=bool,
            ),
            cls(
                SyntaxKind.BangEqualToken,
                BoundBinaryOperatorKind.NotEquals,
                int,
                type=bool,
            ),
            # logical operators
            cls(
                SyntaxKind.AmpersandAmpersandToken,
                BoundBinaryOperatorKind.LogicalAnd,
                bool,
            ),
            cls(SyntaxKind.PipePipeToken, BoundBinaryOperatorKind.LogicalOr, bool),
            cls(SyntaxKind.EqualEqualToken, BoundBinaryOperatorKind.Equals, bool),
            cls(SyntaxKind.BangEqualToken, BoundBinaryOperatorKind.NotEquals, bool),
        ]

    @classmethod
    def bind(cls, kind, left_type, right_type):
        for op in cls.__operators:
            if (
                op.syntax_kind == kind
                and op.left_type == left_type
                and op.right_type == right_type
            ):
                return op
        return None
