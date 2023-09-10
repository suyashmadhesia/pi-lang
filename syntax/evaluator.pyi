from .abstract.expression_syntax import ExpressionSyntax


class Evaluator:

    def __init__(self, root: ExpressionSyntax) -> None: ...

    def evaluate(self) -> int: ...

    def __evaluate_expression(self, node: ExpressionSyntax) -> int: ...

    