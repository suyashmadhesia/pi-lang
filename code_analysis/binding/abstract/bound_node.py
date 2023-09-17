from abc import ABC, abstractproperty

from .bound_node_kind import BoundNodeKind


class BoundNode(ABC):
    @abstractproperty
    def kind(self) -> BoundNodeKind:
        ...
