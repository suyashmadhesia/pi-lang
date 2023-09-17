from binding.abstract.bound_unary_operator_kind import BoundUnaryOperatorKind
from syntax.abstract.syntax_kind import SyntaxKind


class BoundUnaryOperator:

    __operators = []

    def __init__(self, syntax_kind, kind, operand_type, result_type=None):
        self.__syntax_kind = syntax_kind
        self.__operand_type = operand_type
        self.__type = result_type if result_type is not None else operand_type
        self.__kind = kind

    @property
    def operand_type(self):
        return self.__operand_type

    @property
    def type(self):
        return self.__type

    @property
    def kind(self):
        return self.__kind

    @property
    def syntax_kind(self):
        return self.__syntax_kind
    
    @classmethod
    def initialize_operators(cls):
        cls.__operators = [
        cls(SyntaxKind.PlusToken,
                             BoundUnaryOperatorKind.Identity, int),
        cls(SyntaxKind.MinusToken,
                             BoundUnaryOperatorKind.Negation, int)
    ]

    @classmethod
    def bind(cls, kind, operand_type):
        for op in cls.__operators:
            if op.syntax_kind == kind and op.operand_type == operand_type:
                return op
        return None
