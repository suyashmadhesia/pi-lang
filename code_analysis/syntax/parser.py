from typing import List
from .abstract.syntax_kind import SyntaxKind
from .binary_expression_syntax import BinaryExpressionSyntax
from .generics.ie_enumerable import IEnumerable
from .lexer import Lexer
from .literal_expression_syntax import LiteralExpressionSyntax
from .parenthesized_expression_syntax import ParenthesizedExpressionSyntax
from .syntax_facts import SyntaxFacts

from .syntax_token import SyntaxToken
from .syntax_tree import SyntaxTree
from .unary_expression_syntax import UnaryExpressionSyntax


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
        self.__diagnostics.append(
            f"ERROR: Unexpected token <{self.current.kind.name}> expected <{kind.name}>")
        return SyntaxToken(kind, self.current.position, "")

    def parse(self):
        expression = self.__parse_expression()
        end_of_file_token = self.__match_token(SyntaxKind.EndOfFileToken)
        return SyntaxTree(self.diagnostics, expression, end_of_file_token)

    def __parse_expression(self, parent_precedence=0):
        left = None
        unary_operator_precdence = SyntaxFacts.get_unary_operator_precedence(
            self.current.kind)
        if unary_operator_precdence != 0 and unary_operator_precdence >= parent_precedence:
            operator_token = self.__next_token()
            operand = self.__parse_expression(unary_operator_precdence)
            left = UnaryExpressionSyntax(operator_token, operand)
        else:
            left = self.__parse_primary_expression()
        while True:
            binary_operator_precedence = SyntaxFacts.get_binary_operator_precedence(
                self.current.kind)
            if binary_operator_precedence == 0 or binary_operator_precedence <= parent_precedence:
                break
            operator_token = self.__next_token()
            right = self.__parse_expression(binary_operator_precedence)
            left = BinaryExpressionSyntax(left, operator_token, right)
        return left

    def __parse_primary_expression(self):
        if self.current.kind == SyntaxKind.OpenParenthesisToken:
            left = self.__next_token()
            expression = self.__parse_expression()
            right = self.__match_token(SyntaxKind.CloseParenthesisToken)
            return ParenthesizedExpressionSyntax(left, expression, right)
        number_token = self.__match_token(SyntaxKind.NumberToken)
        return LiteralExpressionSyntax(number_token)
