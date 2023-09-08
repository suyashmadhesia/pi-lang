from enum import Enum


class SyntaxKind(Enum):
    EndOfFileToken = 0
    NumberToken = 1
    WhiteSpaceToken = 2
    PlusToken = 3
    MinusToken = 4
    StarToken = 5
    SlashToken = 6
    BadToken = 7
