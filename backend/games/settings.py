from enum import Enum


class Chess(int, Enum):
    PAWN = 1
    KNIGHT = 2
    QUEEN = 3
    BISHOP = 4
    ROOK = 5
    KING = 6

class Color(int, Enum):
    BLACK = 1
    WHITE = 2
