
# default position of chess on board

PAWNS_BLACK_POS = [[x,1] for x in range(0,7)]
KING_BLACK_POS = [4,0]
QUEEN_BLACK_POS = [3,0]
ROOKS_BLACK_POS = [[0,0], [7,0]]
BISHOPS_BLACK_POS = [[2,0], [5,0]]
KNIGHTS_BLACK_POS = [[1,0], [6,0]]


PAWNS_WHITE_POS = [[x,6] for x in range(0,7)]
KING_WHITE_POS = [4,7]
QUEEN_WHITE_POS = [3,7]
ROOKS_WHITE_POS = [[0,7], [7,7]]
BISHOPS_WHITE_POS = [[2,7],[5,7]]
KNIGHTS_WHITE_POS = [[1,7], [6,7]]


# callable params, ArrayField need params in that form

def get_black_pawns():
    return PAWNS_BLACK_POS

def get_white_pawns():
    return PAWNS_WHITE_POS

def get_black_king():
    return KING_BLACK_POS 

def get_white_king():
    return KING_WHITE_POS 

def get_black_queen():
    return QUEEN_BLACK_POS

def get_white_queen():
    return QUEEN_WHITE_POS

def get_black_rooks():
    return ROOKS_BLACK_POS

def get_white_rooks():
    return ROOKS_WHITE_POS

def get_black_bishops():
    return BISHOPS_BLACK_POS

def get_white_bishops():
    return BISHOPS_WHITE_POS

def get_black_knights():
    return KNIGHTS_BLACK_POS

def get_white_knights():
    return KNIGHTS_WHITE_POS
