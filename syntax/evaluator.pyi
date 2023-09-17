from binding.abstract.bound_expression import BoundExpression
from .abstract.expression_syntax import ExpressionSyntax

class Evaluator:

    def __init__(self, root: BoundExpression) -> None: ...

    def evaluate(self) -> int: ...

    def __evaluate_expression(self, node: BoundExpression) -> int | any: ...
