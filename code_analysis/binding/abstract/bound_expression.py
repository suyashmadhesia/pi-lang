from abc import ABC, abstractproperty


class BoundExpression(ABC):
    @abstractproperty
    def type(self) -> any:
        ...
