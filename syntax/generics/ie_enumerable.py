from typing import Iterable, TypeVar

T = TypeVar('T')


class IEnumerable(Iterable[T]):
    def __init__(self, data: Iterable[T]) -> None:
        self.__data = data
        self.__index = 0

    def __iter__(self) -> 'IEnumerable[T]':
        return self

    def __next__(self) -> T:
        if self.__index < len(self.__data):
            result = self.__data[self.__index]
            self.__index += 1
            return result
        else:
            self.__index = 0
            raise StopIteration

    def any(self) -> bool:
        return len(self.__data) > 0

    def last_or_default(self, default_value: T = None) -> bool:
        return self.__data[-1] if self.any() else default_value
