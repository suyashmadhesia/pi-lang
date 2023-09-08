class IEnumerable:
    def __init__(self, data: any) -> None:
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            self.index = 0
            raise StopIteration
