from syntax_token import SyntaxToken

class Lexer:

    def __init__(self, text: str) -> None: ...

    def __peek(self, offset: int) -> chr: ...

    def lex(self) -> SyntaxToken: ...

    def next(self) -> None: ...