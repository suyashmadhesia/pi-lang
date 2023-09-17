from email.parser import Parser
from .abstract.expression_syntax import ExpressionSyntax
from .generics.ie_enumerable import IEnumerable
from .syntax_token import SyntaxToken


class SyntaxTree:

    def __init__(
        self, diagnostics: IEnumerable[str], root: ExpressionSyntax, end_of_file_token: SyntaxToken) -> None: ...

    @property
    def diagnostics(self) -> IEnumerable[str]: ...

    @property
    def root(self) -> ExpressionSyntax: ...

    @property
    def endOfFileToken(self) -> SyntaxToken: ...

    @staticmethod
    def parse(parser: Parser) -> 'SyntaxTree': ...
