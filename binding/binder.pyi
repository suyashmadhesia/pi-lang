from binding.abstract.bound_expression import BoundExpression
from syntax.abstract.expression_syntax import ExpressionSyntax
from syntax.binary_expression_syntax import BinaryExpressionSyntax
from syntax.generics.ie_enumerable import IEnumerable
from syntax.literal_expression_syntax import LiteralExpressionSyntax
from syntax.unary_expression_syntax import UnaryExpressionSyntax


class Binder:

    def __init__(self, syntax: ExpressionSyntax) -> None: ...

    @property
    def diagnostics(self) -> IEnumerable['str']: ...

    def bind_unary_expression(
        self, syntax: UnaryExpressionSyntax) -> BoundExpression: ...

    def bind_binary_expression(
        self, syntax: BinaryExpressionSyntax) -> BoundExpression: ...
    
    def bind_literal_expression(self, syntax: LiteralExpressionSyntax) -> BoundExpression: ...
