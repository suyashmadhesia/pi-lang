from .abstract.syntax_kind import SyntaxKind


class SyntaxFacts:

    @staticmethod
    def get_binary_operator_precedence(kind: SyntaxKind) -> int: ...

    @staticmethod
    def get_unary_operator_precedence(kind: SyntaxKind) -> int: ...