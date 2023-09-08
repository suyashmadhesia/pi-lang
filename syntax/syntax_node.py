from abc import ABC, abstractmethod


class SyntaxNode(ABC):

    @property
    @abstractmethod
    def kind(self):
        ...

    @abstractmethod
    def get_children(self):
        ...
