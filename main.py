import os


from syntax.syntax_tree import SyntaxTree


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
        syntax_tree = SyntaxTree.parse(line)
        diagnostics = syntax_tree.diagnostics
        if not diagnostics.any():
            continue
        else:
            for diagnostic in diagnostics:
                print(diagnostic)


if __name__ == "__main__":
    main()
