from typing import List

from utils.generics import IEnumerable
from syntax_kind import SyntaxKind


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
            return ';'
        return self.__text[index]

    def next(self):
        self.__position += 1

    def lex(self):
        if self.__position >= len(self.__text):
            return SyntaxKind.EndOfFileToken

        if self.current.is_digit():
            start: int = self.__position
            while self.current.is_digit():
                self.next()
            length: int = self.__position - start
            value: str = self.__text[start:length]
            try:
                value = int(value)
                return SyntaxKind.NumberToken
            except:
                self.__diagnostics.append(f'Invalid int at {start}')

        if self.current.isspace():
            while self.current.isspace():
                self.next()
            length: int = self.__position - start
            value: str = self.__text[start:length]
            return SyntaxKind.WhitespaceToken

        if self.current == '+':
            self.next()
            return SyntaxKind.PlusToken
        if self.current == '-':
            self.next()
            return SyntaxKind.MinusToken
        if self.current == '*':
            self.next()
            return SyntaxKind.StarToken
        if self.current == '/':
            self.next()
            return SyntaxKind.SlashToken
        self.__diagnostics.append(
            f'ERROR: Bad Token found on position {self.__position}')
        self.next()
        return SyntaxKind.BadToken
