class SyntaxTree:

    def __init__(self, diagnostics, root, end_of_file_token):
        self.__diagnostics = diagnostics
        self.__root = root
        self.__end_of_file_token = end_of_file_token

    @property
    def diagnostics(self):
        return self.__diagnostics

    @property
    def root(self):
        return self.__root

    @property
    def end_of_file_token(self):
        return self.__end_of_file_token

    @staticmethod
    def parse(text):
        ...
