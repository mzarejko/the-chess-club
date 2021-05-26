
def check_if_everything_in_range(moves):
    ref = list(moves.copy())
    for move in moves:
        if move < 0 or move > 63:
            ref.remove(move)
    return ref
 
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
 
 
def update_moves(positions, move, my_piece, enemies, moves, attack):
    for pos in positions:
        if check_obstacles(pos+move, enemies):
            attack+= [pos+move]
            break
        elif not check_obstacles(pos+move, my_piece):
            moves+= [pos+move]
    
    return moves, attack

class PieceMoves:

    @staticmethod
    def get_white_pawn_moves(pos, my_piece, enemies, first=False):
        moves = []
        attack = []
        if first:
            if check_obstacles(pos-9, enemies):
                attack+= [pos-9]
            if check_obstacles(pos-7, enemies):
                attack+= [pos-7]
            if not check_obstacles(pos-8, my_piece) and not check_obstacles(pos-8, enemies):
                moves += [pos-8]

            if not check_obstacles(pos-16, my_piece) and not check_obstacles(pos-16, enemies):
                moves+= [pos-16]
        else:
            if check_obstacles(pos-9, enemies):
                attack+= [pos-9]
            if check_obstacles(pos-7, enemies):
                attack+= [pos-7]
            if not check_obstacles(pos-8, my_piece) and not check_obstacles(pos-8, enemies):
                moves += [pos-8]

        moves = check_if_everything_in_range(moves)
        attack = check_if_everything_in_range(attack)
        return moves, attack 

    @staticmethod
    def get_black_pawn_moves(pos, my_piece, enemies, first=False):
        moves = []
        attack = []
        if first:
            if check_obstacles(pos+9, enemies):
                attack+= [pos+9]
            if check_obstacles(pos+7, enemies):
                attack+= [pos+7]
            if not check_obstacles(pos+8, my_piece) and not check_obstacles(pos+8, enemies):
                moves += [pos+8]
        else:
            if check_obstacles(pos+9, enemies):
                attack+= [pos+9]
            if check_obstacles(pos+7, enemies):
                attack+= [pos+7]
            if not check_obstacles(pos+8, my_piece) and not check_obstacles(pos+8, enemies):
                moves += [pos+8]

        moves = check_if_everything_in_range(moves)
        attack = check_if_everything_in_range(attack)
         
        return moves, attack
        
    
    @staticmethod
    def get_bishop_moves(pos, my_piece, enemies):
        moves = []
        attack = []

        moves, attack = update_moves([x for x in range(9, 64, 9)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(-9, -64, -9)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(7, 64, 7)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(-7, -64, -7)], pos, my_piece, enemies, moves, attack)
        moves = check_if_everything_in_range(moves)
        attack = check_if_everything_in_range(attack)
        return moves, attack
    
    @staticmethod
    def get_rook_moves(pos, my_piece, enemies):
        moves = []
        attack = []

        moves, attack = update_moves([x for x in range(8, 64, 8)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(-8, -64, -8)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(1, 8)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(-1, -8, -1)], pos, my_piece, enemies, moves, attack)
        moves = check_if_everything_in_range(moves)
        attack = check_if_everything_in_range(attack)
        return moves, attack
    
    @staticmethod
    def get_queen_moves(pos, my_piece, enemies):
        moves = []
        attack = []

        moves, attack = update_moves([x for x in range(8, 64, 8)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(-8, -64, -8)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(1, 8)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(-1, -8, -1)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(9, 64, 9)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(-9, -64, -9)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(7, 64, 7)], pos, my_piece, enemies, moves, attack)
        moves, attack = update_moves([x for x in range(-7, -64, -7)], pos, my_piece, enemies, moves, attack)

        moves = check_if_everything_in_range(moves)
        attack = check_if_everything_in_range(attack)
        return moves, attack
    
    @staticmethod
    def get_knight_moves(pos, my_piece, enemies):
        moves = []
        attack = []

        if check_obstacles(pos-15, enemies):
            attack+= [pos-15]
        elif not check_obstacles(pos-15, my_piece):
            moves += [pos-15]

        if check_obstacles(pos-17, enemies):
            attack+= [pos-17]
        elif not check_obstacles(pos-17, my_piece):
            moves += [pos-17]

        if check_obstacles(pos+15, enemies):
            attack+= [pos+15]
        elif not check_obstacles(pos+15, my_piece):
            moves += [pos+15]

        if check_obstacles(pos+17, enemies):
            attack+= [pos+17]
        elif not check_obstacles(pos+17, my_piece):
            moves += [pos+17]

        moves = check_if_everything_in_range(moves)
        attack = check_if_everything_in_range(attack)
        return moves, attack
    
    @staticmethod
    def get_king_moves(pos, my_piece, enemies):
        moves = []
        attack = []

        if check_obstacles(pos-1, enemies):
            attack+= [pos-1]
        elif not check_obstacles(pos-1, my_piece):
            moves += [pos-1]

        if check_obstacles(pos-8, enemies):
            attack+= [pos-8]
        elif not check_obstacles(pos-8, my_piece):
            moves += [pos-8]

        if check_obstacles(pos+1, enemies):
            attack+= [pos+1]
        elif not check_obstacles(pos+1, my_piece):
            moves += [pos+1]

        if check_obstacles(pos+8, enemies):
            attack+= [pos+8]
        elif not check_obstacles(pos+8, my_piece):
            moves += [pos+8]

        if check_obstacles(pos+9, enemies):
            attack+= [pos+9]
        elif not check_obstacles(pos+9, my_piece):
            moves += [pos+9]

        if check_obstacles(pos-9, enemies):
            attack+= [pos-9]
        elif not check_obstacles(pos-9, my_piece):
            moves += [pos-9]

        if check_obstacles(pos+7, enemies):
            attack+= [pos+7]
        elif not check_obstacles(pos+7, my_piece):
            moves += [pos+7]

        if check_obstacles(pos-7, enemies):
            attack+= [pos-7]
        elif not check_obstacles(pos-7, my_piece):
            moves += [pos-7]

        moves = check_if_everything_in_range(moves)
        attack = check_if_everything_in_range(attack)
        return moves, attack

