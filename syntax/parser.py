from typing import List

from .generics.ie_enumerable import IEnumerable
from .lexer import Lexer
from .syntax_token import SyntaxToken
from .abstract.syntax_kind import SyntaxKind


class Parser:

    def __init__(self, text):
        self.__tokens: List[SyntaxToken] = []
        self.__diagnostics: List[str] = []
        self.__position: int = 0
        lexer = Lexer(text)
        while True:
            token = lexer.lex()
            if token.kind not in {SyntaxKind.WhiteSpaceToken, SyntaxKind.BadToken}:
                self.__tokens.append(token)
            if token.kind == SyntaxKind.EndOfFileToken:
                break
        self.__diagnostics.extend(lexer.diagnostics)

    @property
    def diagnostics(self):
        return IEnumerable(self.__diagnostics)
    
    def __peek(self, offset):
        index: int = self.__position + offset
        while index >= len(self.__tokens):
            return self.__tokens[-1]
        return self.__tokens[index]

    @property
    def current(self):
        return self.__peek(0)

    def __next_token(self):
        _current = self.current
        self.__position += 1
        return _current
    

    def __match_token(self, kind):
        if self.current.kind == kind:
            return self.__next_token()
        self.__diagnostics.append(f"ERROR: Unexpected token <{self.current.kind.name}> expected <{kind.name}>")
        return SyntaxToken(kind, self.current.position, "")

