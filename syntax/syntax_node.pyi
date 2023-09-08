from abc import ABC, abstractmethod
from .syntax_kind import SyntaxKind
from utils.generics import IEnumerable

class SyntaxNode(ABC):

    @property
    @abstractmethod
    def kind(self) -> SyntaxKind: ...

    @abstractmethod
    def get_children(self) -> IEnumerable['SyntaxNode']: ...
