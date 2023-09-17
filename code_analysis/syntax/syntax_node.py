from abc import ABC, abstractmethod, abstractproperty


class SyntaxNode(ABC):
    @abstractproperty
    def kind(self):
        ...

    @abstractmethod
    def get_children(self):
        ...
