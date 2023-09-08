import os


from syntax.lexer import Lexer
from syntax.syntax_kind import SyntaxKind


def __clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        tokens = []
        diagnostics = []
        line = str(input(">>> "))
        if line == "clear":
            __clear()
            continue
        if line == "exit":
            break
        lexer = Lexer(line)
        while True:
            token = lexer.lex()
            if token.kind not in {SyntaxKind.WhiteSpaceToken, SyntaxKind.BadToken}:
                tokens.append(token)
            if token.kind == SyntaxKind.EndOfFileToken:
                break
        for d in lexer.diagnostics:
            diagnostics.append(d)
        if len(diagnostics) > 0:
            for d in diagnostics:
                print(d)
            continue
        print(tokens)

        


if __name__ == "__main__":
    main()
