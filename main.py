import os

from code_analysis.binding.binder import Binder
from code_analysis.evaluator import Evaluator
from code_analysis.syntax.generics.ie_enumerable import IEnumerable
from code_analysis.syntax.parser import Parser
from code_analysis.syntax.syntax_node import SyntaxNode
from code_analysis.syntax.syntax_token import SyntaxToken
from code_analysis.syntax.syntax_tree import SyntaxTree


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
    tree = False
    while True:
        diagnostics: IEnumerable[str] = []
        line = str(input(">>> "))
        if line == "clear":
            clear()
            continue
        if line == "exit":
            break
        if line == "tree":
            write_line("Showing parse tree")
            tree = not tree
            continue
        parser = Parser(line)
        syntax_tree = SyntaxTree.parse(parser)
        binder = Binder()
        bound_expression = binder.bind_expression(syntax_tree.root)
        diagnostics = syntax_tree.diagnostics
        if tree:
            show_parse_tree(syntax_tree.root)
        if not diagnostics.any():
            evaluator = Evaluator(bound_expression)
            result = evaluator.evaluate()
            write_line(result)
        else:
            for diagnostic in diagnostics:
                write_line(diagnostic)


if __name__ == "__main__":
    main()
