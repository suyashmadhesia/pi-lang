from typing import List

from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable
from .syntax_token import SyntaxToken
from .syntax_facts import SyntaxFacts


class Lexer:
    def __init__(self, text):
        self.__text: str = text
        self.__position: int = 0
        self.__diagnostics: List[str] = []

    @property
    def diagnostics(self):
        return IEnumerable(self.__diagnostics)

    @property
    def current(self):
        return self.__peek(0)

    def __peek(self, offset: int):
        index: int = self.__position + offset
        if index >= len(self.__text):
            return "\0"
        return self.__text[index]

    def __next(self):
        self.__position += 1

    @property
    def __lookahead(self):
        return self.__peek(1)

    def lex(self):
        if self.__position >= len(self.__text):
            return SyntaxToken(SyntaxKind.EndOfFileToken, self.__position, "\0")

        if self.current.isdigit():
            start: int = self.__position
            while self.current.isdigit():
                self.__next()
            text: str = self.__text[start : self.__position]
            try:
                value: int = int(text)
                return SyntaxToken(SyntaxKind.NumberToken, start, text, value)
            except:
                self.__diagnostics.append(f"Invalid int at {start}")

        if self.current.isspace() or not len(self.current):
            start: int = self.__position
            while self.current.isspace() or not len(self.current):
                self.__next()
            value: str = self.__text[start : self.__position]
            return SyntaxToken(SyntaxKind.WhiteSpaceToken, start, self.__text)

        if self.current.isalpha():
            start: int = self.__position
            while self.current.isalpha():
                self.__next()
            text: str = self.__text[start : self.__position]
            kind = SyntaxFacts.get_keyword_kind(text)
            return SyntaxToken(kind, start, text)

        if self.current == "+":
            self.__next()
            return SyntaxToken(SyntaxKind.PlusToken, self.__position, "+")
        if self.current == "-":
            self.__next()
            return SyntaxToken(SyntaxKind.MinusToken, self.__position, "-")
        if self.current == "*":
            self.__next()
            return SyntaxToken(SyntaxKind.StarToken, self.__position, "*")
        if self.current == "/":
            self.__next()
            return SyntaxToken(SyntaxKind.SlashToken, self.__position, "/")
        if self.current == "(":
            self.__next()
            return SyntaxToken(SyntaxKind.OpenParenthesisToken, self.__position, "(")
        if self.current == ")":
            self.__next()
            return SyntaxToken(SyntaxKind.CloseParenthesisToken, self.__position, ")")
        if self.current == "&":
            if self.__lookahead == "&":
                self.__next()
                self.__next()
                return SyntaxToken(
                    SyntaxKind.AmpersandAmpersandToken, self.__position, "&&"
                )
        if self.current == "|":
            if self.__lookahead == "|":
                self.__next()
                self.__next()
                return SyntaxToken(SyntaxKind.PipePipeToken, self.__position, "||")
        if self.current == "=":
            if self.__lookahead == "=":
                self.__next()
                self.__next()
                return SyntaxToken(SyntaxKind.EqualEqualToken, self.__position, "==")
        if self.current == "!":
            if self.__lookahead == "=":
                self.__next()
                self.__next()
                return SyntaxToken(SyntaxKind.BangEqualToken, self.__position, "!=")
            self.__next()
            return SyntaxToken(SyntaxKind.BangToken, self.__position, "!")
        self.__diagnostics.append(
            f"ERROR: Bad Token found on position {self.__position}"
        )
        self.__next()
        return SyntaxToken(SyntaxKind.BadToken, self.__position, self.__text[-1])
