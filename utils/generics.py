from typing import Iterable, TypeVar
T = TypeVar('T')


class IEnumerable(Iterable[T]):
    def __init__(self, data: Iterable[T]) -> None:
        self.data = data
        self.index = 0

    def __iter__(self) -> 'IEnumerable[T]':
        return self

    def __next__(self) -> T:
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            self.index = 0
            raise StopIteration
