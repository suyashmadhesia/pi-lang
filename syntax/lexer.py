from typing import List

from utils.ie_numberable import IEnumerable
from . syntax_kind import SyntaxKind


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

    def __peek(self, offset):
        index: int = self.__position + offset
        if index >= len(self.__text):
            return '\0'
        return self.__text[index]

    def __next(self):
        self.__position += 1

    def lex(self):
        if self.__position >= len(self.__text):
            return SyntaxKind.EndOfFileToken

        if self.current.isdigit():
            start: int = self.__position
            while self.current.isdigit():
                self.__next()
            value: str = self.__text[start:self.__position]
            try:
                value = int(value)
                return SyntaxKind.NumberToken
            except:
                self.__diagnostics.append(f'Invalid int at {start}')

        if self.current.isspace() or not len(self.current):
            start: int = self.__position
            while self.current.isspace() or not len(self.current):
                self.__next()
            value: str = self.__text[start:self.__position]
            return SyntaxKind.WhiteSpaceToken

        if self.current == '+':
            self.__next()
            return SyntaxKind.PlusToken
        if self.current == '-':
            self.__next()
            return SyntaxKind.MinusToken
        if self.current == '*':
            self.__next()
            return SyntaxKind.StarToken
        if self.current == '/':
            self.__next()
            return SyntaxKind.SlashToken
        self.__diagnostics.append(
            f'ERROR: Bad Token found on position {self.__position}')
        self.__next()
        return SyntaxKind.BadToken
