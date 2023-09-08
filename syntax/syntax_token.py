from .syntax_node import SyntaxNode


class SyntaxToken(SyntaxNode):

    def __init__(self, kind, position, text, value=None) -> None:
        self.__kind = kind
        self.__position = position
        self.__text = text
        self.__value = value

    @property
    def kind(self):
        return self.__kind

    @property
    def position(self):
        return self.__position

    @property
    def text(self):
        return self.__text

    @property
    def value(self):
        return self.__value

    def get_children(self):
        return []
