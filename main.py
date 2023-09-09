import os

from syntax.syntax_node import SyntaxNode
from syntax.syntax_token import SyntaxToken
from syntax.syntax_tree import SyntaxTree
from syntax.generics.ie_enumerable import IEnumerable


def write(data: any = ""):
    print(data, end="")


def write_line(data: any = ""):
    print(data, end="\n")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def show_parse_tree(node: SyntaxNode, indent: str = "", is_last: bool = True):
    marker = "└──" if is_last else "├──"
    write(f"{indent}{marker}{node.kind}")
    if type(node) == SyntaxToken and node.value != None:
        write(f" {node.value}")
    write_line()
    indent += "   " if is_last else "│   "
    last_child = node.get_children().last_or_default()
    for child in node.get_children():
        show_parse_tree(child, indent, child == last_child)


def main():
    while True:
        diagnostics: IEnumerable[str] = []
        line = str(input(">>> "))
        if line == "clear":
            clear()
            continue
        if line == "exit":
            break
        syntax_tree = SyntaxTree.parse(line)
        diagnostics = syntax_tree.diagnostics
        if not diagnostics.any():
            show_parse_tree(syntax_tree.root)
        else:
            for diagnostic in diagnostics:
                write_line(diagnostic)


if __name__ == "__main__":
    main()
