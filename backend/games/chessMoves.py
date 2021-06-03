from enum import Enum

class PieceMovesAttack(list, Enum):
    PAWNS_WHITE_SECOND = [[[-1,0]]]
    PAWNS_WHITE_FIRST = [[[-1,0]], [[-2,0]]]
    PAWNS_WHITE_ATTACK = [[[-1,-1]],[[-1, 1]]]

    PAWNS_BLACK_SECOND = [[[1, 0]]]
    PAWNS_BLACK_FIRST = [[[1, 0]], [[2,0]]]
    PAWNS_BLACK_ATTACK = [[[1,-1]], [[1,1]]]

    BISHOP_MOVES_ATTACKS = [[[x,x] for x in range(1, 7)],
                            [[-x,-x] for x in range(1, 7)],
                            [[x,-x] for x in range(1, 7)],
                            [[-x,x] for x in range(1, 7)]]

    ROOK_MOVES_ATTACKS = [[[0,x] for x in range(1,7)],
                          [[x,0] for x in range(1,7)],
                          [[0,-x] for x in range(1,7)],
                          [[-x,0] for x in range(1,7)]]
    
    QUEEN_MOVES_ATTACKS = [[[0,x] for x in range(1,7)],
                           [[x,0] for x in range(1,7)],
                           [[0,-x] for x in range(1,7)],
                           [[-x,0] for x in range(1,7)],
                           [[x,x] for x in range(1,7)],
                           [[-x,-x] for x in range(1,7)],
                           [[x,-x] for x in range(1,7)],
                           [[-x,x] for x in range(1,7)]]
    
    KNIGHT_MOVES_ATTACKS = [[[-2,-1]], [[-2,1]], [[2,-1]], [[2,1]], [[1, 2]], [[-1, 2]], [[-1,-2]], [[1,-2]]]
    KING_MOVES_ATTACKS = [[[0,1]], [[1,0]], [[1,1]], [[-1,0]], [[0,-1]], [[1,-1]], [[-1,1]], [[-1,-1]]]
 
def check_obstacles(ref, pieces):
    for pos in pieces.pawns:
        if pos == ref:
            return True
    for pos in pieces.knights:
        if pos == ref:
            return True
    for pos in pieces.king:
        if pos == ref:
            return True
    for pos in pieces.queen:
        if pos == ref:
            return True
    for pos in pieces.rooks:
        if pos == ref:
            return True
    for pos in pieces.queen:
        if pos == ref:
            return True
    for pos in pieces.bishops:
        if pos == ref:
            return True
    return False
 
 
def update_moves(positions, offset, my_piece, enemies, moves, attack):
    for pos in positions:
        numeric_pos = pos[0]*8+pos[1]
        dimension_offset = [offset/8, offset%8]
        output_pos_dimension = [pos[0]+dimension_offset[0], 
                                pos[1]+dimension_offset[1]]
        
        # check if move will not go out of array scope
        if output_pos_dimension[0]>7 or output_pos_dimension[1]>7 or\
            output_pos_dimension[0]< 0 or output_pos_dimension[1]<0:
                break

        if check_obstacles(numeric_pos+offset, enemies):
            next_pos = numeric_pos+offset
            
            if next_pos>=0 and next_pos<64:
                attack+= [next_pos]
            break
        elif not check_obstacles(numeric_pos+offset, my_piece):
            next_pos = numeric_pos+offset

            if next_pos>=0 and next_pos<64:
                moves+= [next_pos]
            else:
                break
        else:
            break
    
    return moves, attack


def check_if_everything_in_range(moves):
    ref = list(moves.copy())
    for move in moves:
        if move < 0 or move > 63:
            ref.remove(move)
    return ref

class PieceMoves:

    @staticmethod
    def get_white_pawn_moves(offset, my_piece, enemies, first=False):
        moves = []
        attack = []

        for poses in PieceMovesAttack.PAWNS_WHITE_ATTACK:
            _, attack = update_moves(poses, offset, my_piece, enemies, [], attack)

        if first:
            for poses in PieceMovesAttack.PAWNS_WHITE_FIRST:
                moves, attack = update_moves(poses, offset, my_piece, enemies, moves, attack)
        else:
            for poses in PieceMovesAttack.PAWNS_WHITE_SECOND:
                moves, attack = update_moves(poses, offset, my_piece, enemies, moves, attack)

        return moves, attack 

    @staticmethod
    def get_black_pawn_moves(offset, my_piece, enemies, first=False):
        moves = []
        attack = []
        for poses in PieceMovesAttack.PAWNS_BLACK_ATTACK:
            _, attack = update_moves(poses, offset, my_piece, enemies, [], attack)
        
        if first:
            for poses in PieceMovesAttack.PAWNS_BLACK_FIRST:
                moves, attack = update_moves(poses, offset, my_piece, enemies, moves, attack)
        else:
            for poses in PieceMovesAttack.PAWNS_BLACK_SECOND:
                moves, attack = update_moves(poses, offset, my_piece, enemies, moves, attack)

        return moves, attack
        
    
    @staticmethod
    def get_bishop_moves(offset, my_piece, enemies):
        moves = []
        attack = []

        for poses in PieceMovesAttack.BISHOP_MOVES_ATTACKS:
            moves, attack = update_moves(poses, offset, my_piece, enemies, moves, attack)
        return moves, attack
    
    @staticmethod
    def get_rook_moves(offset, my_piece, enemies):
        moves = []
        attack = []

        for poses in PieceMovesAttack.ROOK_MOVES_ATTACKS:
            moves, attack = update_moves(poses, offset, my_piece, enemies, moves, attack)
        return moves, attack
    
    @staticmethod
    def get_queen_moves(offset, my_piece, enemies):
        moves = []
        attack = []

        for poses in PieceMovesAttack.QUEEN_MOVES_ATTACKS:
            moves, attack = update_moves(poses, offset, my_piece, enemies, moves, attack)

        return moves, attack
    
    @staticmethod
    def get_knight_moves(offset, my_piece, enemies):
        moves = []
        attack = []
        
        for poses in PieceMovesAttack.KNIGHT_MOVES_ATTACKS:
            moves, attack = update_moves(poses, offset, my_piece, enemies, moves, attack)

        return moves, attack
    
    @staticmethod
    def get_king_moves(offset, my_piece, enemies):
        moves = []
        attack = []

        for poses in PieceMovesAttack.KING_MOVES_ATTACKS:
            moves, attack = update_moves(poses, offset, my_piece, enemies, moves, attack)

        return moves, attack

