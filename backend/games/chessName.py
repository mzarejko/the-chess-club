from enum import Enum


class Pieces(str, Enum):
    PAWN = 'pawns'
    KNIGHT = 'knights'
    QUEEN = 'queen'
    BISHOP = 'bishops'
    ROOK = 'rooks'
    KING = 'king'

