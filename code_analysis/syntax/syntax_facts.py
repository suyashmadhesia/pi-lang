from .abstract.syntax_kind import SyntaxKind


class SyntaxFacts:
    @staticmethod
    def get_unary_operator_precedence(kind):
        if (
            kind == SyntaxKind.PlusToken
            or kind == SyntaxKind.MinusToken
            or kind == SyntaxKind.BangToken
        ):
            return 6
        return 0

    @staticmethod
    def get_binary_operator_precedence(kind):
        if kind == SyntaxKind.StarToken or kind == SyntaxKind.SlashToken:
            return 5
        if kind == SyntaxKind.PlusToken or kind == SyntaxKind.MinusToken:
            return 4
        if kind == SyntaxKind.EqualEqualToken or kind == SyntaxKind.BangEqualToken:
            return 3
        if kind == SyntaxKind.AmpersandAmpersandToken:
            return 2
        if kind == SyntaxKind.PipePipeToken:
            return 1
        return 0

    @staticmethod
    def get_keyword_kind(text):
        if text == "true":
            return SyntaxKind.TrueKeywordToken
        if text == "false":
            return SyntaxKind.FalseKeywordToken
        return SyntaxKind.IdentifierToken
