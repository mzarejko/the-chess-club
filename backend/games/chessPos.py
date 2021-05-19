
# default position of chess on board 8x8 = 64 positions

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
