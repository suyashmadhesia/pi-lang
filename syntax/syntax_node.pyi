from abc import ABC, abstractmethod

from .abstract.syntax_kind import SyntaxKind
from .generics.ie_enumerable import IEnumerable

class SyntaxNode(ABC):

    @property
    @abstractmethod
    def kind(self) -> SyntaxKind: ...

    @abstractmethod
    def get_children(self) -> IEnumerable['SyntaxNode']: ...
