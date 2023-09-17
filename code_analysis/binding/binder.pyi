from code_analysis.syntax.abstract.expression_syntax import ExpressionSyntax
from code_analysis.syntax.binary_expression_syntax import BinaryExpressionSyntax
from code_analysis.syntax.generics.ie_enumerable import IEnumerable
from code_analysis.syntax.literal_expression_syntax import LiteralExpressionSyntax
from code_analysis.syntax.unary_expression_syntax import UnaryExpressionSyntax
from .abstract.bound_expression import BoundExpression



class Binder:

    def __init__(self) -> None: ...

    @property
    def diagnostics(self) -> IEnumerable['str']: ...

    def bind_expression(self, syntax: ExpressionSyntax) -> BoundExpression: ...

    def __bind_unary_expression(
        self, syntax: UnaryExpressionSyntax) -> BoundExpression: ...

    def __bind_binary_expression(
        self, syntax: BinaryExpressionSyntax) -> BoundExpression: ...

    def __bind_literal_expression(
        self, syntax: LiteralExpressionSyntax) -> BoundExpression: ...
