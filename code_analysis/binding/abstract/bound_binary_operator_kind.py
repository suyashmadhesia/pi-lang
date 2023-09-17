from enum import Enum


class BoundBinaryOperatorKind(Enum):
    Addition = 0
    Subtraction = 1
    Multiplication = 2
    Division = 3
    LogicalAnd = 4
    LogicalOr = 5
    NotEquals = 6
    Equals = 7
