
def check_if_everything_in_range(moves):
    ref = list(moves.copy())
    for move in moves:
        if move < 0 or move > 63:
            ref.remove(move)
    return ref

def check_obstacles(ref, board):
    for pos in board.pawns:
        if pos == ref:
            return True
    for pos in board.knights:
        if pos == ref:
            return True
    for pos in board.king:
        if pos == ref:
            return True
    for pos in board.queen:
        if pos == ref:
            return True
    for pos in board.rooks:
        if pos == ref:
            return True
    for pos in board.queen:
        if pos == ref:
            return True
    for pos in board.bishops:
        if pos == ref:
            return True
    return False


def update_moves(start, stop, step, pos, board, moves, up=True):
    if step:
         for next_pos in range(start, stop, step):
             if up:
                 if not check_obstacles(pos+next_pos, board):
                     moves+= [pos+next_pos]
                 else:
                     break
             else:
                 if not check_obstacles(pos-next_pos, board):
                     moves+= [pos-next_pos]
                 else:
                     break
    else:
         for next_pos in range(start, stop):
             if up:
                 if not check_obstacles(pos+next_pos, board):
                     moves+= [pos+next_pos]
                 else:
                     break
             else:
                 if not check_obstacles(pos-next_pos, board):
                     moves+= [pos-next_pos]
                 else:
                     break

    return moves


# possible moves
class MovePiece:
    
    @staticmethod
    def get_white_pawn_moves(pos, board, first=False):
        moves = []
        attack = []
        if first:
            if not check_obstacles(pos-8, board):
                moves += [pos-8]
            if not check_obstacles(pos-16, board):
                moves+= [pos-16]
        else:
            if not check_obstacles(pos-8, board):
                moves += [pos-8]
        moves = check_if_everything_in_range(moves)
        return moves 

    @staticmethod
    def get_black_pawn_moves(pos, board, first=False):
        moves = []
        if first:
            if not check_obstacles(pos+8, board):
                moves += [pos+8]
            if not check_obstacles(pos+16, board):
                moves+=[pos+16]
        else:
            if not check_obstacles(pos+8, board):
                moves += [pos+8]
        moves = check_if_everything_in_range(moves)
        return moves 
        
    
    @staticmethod
    def get_bishop_moves(pos, board):
        moves = []
        moves = update_moves(9, 64, 9, pos, board, moves)
        moves = update_moves(9, 64, 9, pos, board, moves, up=False)
        moves = update_moves(7, 64, 7, pos, board, moves)
        moves = update_moves(7, 64, 7, pos, board, moves, up=False)
        moves = check_if_everything_in_range(moves)
        return moves
    
    @staticmethod
    def get_rook_moves(pos, board):
        moves = []
        moves = update_moves(8, 64, 8, pos, board, moves)
        moves = update_moves(8, 64, 8, pos, board, moves, up=False)
        moves = update_moves(1, 8, None, pos, board, moves)
        moves = update_moves(1, 8, None, pos, board, moves, up=False)
        moves = check_if_everything_in_range(moves)
        return moves
    
    @staticmethod
    def get_queen_moves(pos, board):
        moves = []
        moves = update_moves(8, 64, 8, pos, board, moves)
        moves = update_moves(8, 64, 8, pos, board, moves, up=False)
        moves = update_moves(1, 8, None, pos, board, moves)
        moves = update_moves(1, 8, None, pos, board, moves, up=False)
        moves = update_moves(9, 64, 9, pos, board, moves)
        moves = update_moves(9, 64, 9, pos, board, moves, up=False)
        moves = update_moves(7, 64, 7, pos, board, moves)
        moves = update_moves(7, 64, 7, pos, board, moves, up=False)
        moves = check_if_everything_in_range(moves)
        return moves
    
    @staticmethod
    def get_knight_moves(pos, board):
        moves=[]
        if not check_obstacles(pos-15, board):
            moves += [pos-15]
        if not check_obstacles(pos-17, board):
            moves += [pos-17]
        if not check_obstacles(pos+15, board):
            moves += [pos+15]
        if not check_obstacles(pos+17, board):
            moves += [pos+17]
        moves = check_if_everything_in_range(moves)
        return moves
    
    @staticmethod
    def get_king_moves(pos, board):
        moves=[]
        if not check_obstacles(pos-1, board):
            moves += [pos-1]
        if not check_obstacles(pos-8, board):
            moves += [pos-8]
        if not check_obstacles(pos+1, board):
            moves += [pos+1]
        if not check_obstacles(pos+8, board):
            moves += [pos+8]
        if not check_obstacles(pos+9, board):
            moves += [pos+9]
        if not check_obstacles(pos-9, board):
            moves += [pos-9]
        if not check_obstacles(pos+7, board):
            moves += [pos+7]
        if not check_obstacles(pos-7, board):
            moves += [pos-7]
        moves = check_if_everything_in_range(moves)
        return moves

