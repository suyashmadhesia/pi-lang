from .abstract.syntax_kind import SyntaxKind


class SyntaxFacts:
    @staticmethod
    def get_binary_operator_precedence(kind):
        if kind == SyntaxKind.StarToken or kind == SyntaxKind.SlashToken:
            return 2
        if kind == SyntaxKind.PlusToken or kind == SyntaxKind.MinusToken:
            return 1
        return 0

    @staticmethod
    def get_unary_operator_precedence(kind):
        if kind == SyntaxKind.PlusToken or kind == SyntaxKind.MinusToken:
            return 3
        return 0
