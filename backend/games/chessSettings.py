from enum import Enum

class Color(int, Enum):
    WHITE = 1
    BLACK = 2


class PieceMedia(str, Enum):
    BLACK_BISHOP='http://127.0.0.1:8000/media/chess/black/bishop-black-16x16.png'
    BLACK_KING='http://127.0.0.1:8000/media/chess/black/king-black-16x16.png'
    BLACK_KNIGHT='http://127.0.0.1:8000/media/chess/black/knight-black-16x16.png'
    BLACK_PAWN='http://127.0.0.1:8000/media/chess/black/pawn-black-16x16.png'
    BLACK_QUEEN='http://127.0.0.1:8000/media/chess/black/queen-black-16x16.png'
    BLACK_ROOK='http://127.0.0.1:8000/media/chess/black/rook-black-16x16.png'
    
    WHITE_BISHOP='http://127.0.0.1:8000/media/chess/white/bishop-white-16x16.png'
    WHITE_KING='http://127.0.0.1:8000/media/chess/white/king-white-16x16.png'
    WHITE_KNIGHT='http://127.0.0.1:8000/media/chess/white/knight-white-16x16.png'
    WHITE_PAWN='http://127.0.0.1:8000/media/chess/white/pawn-white-16x16.png'
    WHITE_QUEEN='http://127.0.0.1:8000/media/chess/white/queen-white-16x16.png'
    WHITE_ROOK='http://127.0.0.1:8000/media/chess/white/rook-white-16x16.png'

class PiecesNameKeys(str, Enum):
    PAWN = 'pawns'
    KNIGHT = 'knights'
    QUEEN = 'queen'
    BISHOP = 'bishops'
    ROOK = 'rooks'
    KING = 'king'

# default position of chess on board 8x8 = 64 positions
class Positions(list, Enum):
    PAWNS_BLACK_POS = [x for x in range(8,16)]
    KING_BLACK_POS = [3]
    QUEEN_BLACK_POS = [4]
    ROOKS_BLACK_POS = [0,7]
    BISHOPS_BLACK_POS = [2, 5]
    KNIGHTS_BLACK_POS = [1, 6]

    PAWNS_WHITE_POS = [x for x in range(48,56)]
    KING_WHITE_POS = [59]
    QUEEN_WHITE_POS = [60]
    ROOKS_WHITE_POS = [56, 63]
    BISHOPS_WHITE_POS = [61, 58]
    KNIGHTS_WHITE_POS = [62, 57]


# callable params, ArrayField need params in that form
class ArrayFunc:
    @staticmethod
    def get_black_pawns():
        return Positions.PAWNS_BLACK_POS
    
    @staticmethod
    def get_white_pawns():
        return Positions.PAWNS_WHITE_POS
    
    @staticmethod
    def get_black_king():
        return Positions.KING_BLACK_POS 
    
    @staticmethod
    def get_white_king():
        return Positions.KING_WHITE_POS 
    
    @staticmethod
    def get_black_queen():
        return Positions.QUEEN_BLACK_POS
    
    @staticmethod
    def get_white_queen():
        return Positions.QUEEN_WHITE_POS
    
    @staticmethod
    def get_black_rooks():
        return Positions.ROOKS_BLACK_POS
    
    @staticmethod
    def get_white_rooks():
        return Positions.ROOKS_WHITE_POS
    
    @staticmethod
    def get_black_bishops():
        return Positions.BISHOPS_BLACK_POS
    
    @staticmethod
    def get_white_bishops():
        return Positions.BISHOPS_WHITE_POS
    
    @staticmethod
    def get_black_knights():
        return Positions.KNIGHTS_BLACK_POS
    
    @staticmethod
    def get_white_knights():
        return Positions.KNIGHTS_WHITE_POS


