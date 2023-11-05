# chessDictionaryValidator.py

def main(chessBoard):
    if is_valid(chessBoard):
        return("Valid")
    else:
        return("Invalid")

def is_valid(chessBoard):
    if two_kings(chessBoard) and sixteen_pieces(chessBoard) and eight_pawns(chessBoard) and on_a_valid_space(chessBoard) and piece_names(chessBoard):
        return True
    else:
        return False
    
def two_kings(chessBoard):
    white_king_count = 0
    black_king_count = 0
    for piece in chessBoard.values():
        if piece == "wking":
            white_king_count += 1
        elif piece == "bking":
            black_king_count += 1
    if white_king_count == 1 and black_king_count == 1:
        return True
    else:
        return False

def sixteen_pieces(chessBoard):
    white_piece_count = 0
    black_piece_count = 0
    for piece in chessBoard.values():
        if piece[0] == 'w':
            white_piece_count += 1
        elif piece[0] == 'b':
            black_piece_count += 1
    if white_piece_count > 16 or black_piece_count > 16:
        return False
    else:
        return True
    
def eight_pawns(chessBoard):
    white_pawn_count = 0
    black_pawn_count = 0
    for piece in chessBoard.values():
        if piece == 'wpawn':
            white_pawn_count += 1
        elif piece == 'bpawn':
            black_pawn_count += 1
    if white_pawn_count > 8 or black_pawn_count > 8:
        return False
    else:
        return True
    
def on_a_valid_space(chessBoard):
    for piece in chessBoard.keys():
        if piece[0] in "12345678" and piece[1] in "abcdefgh":
            return True
        else:
            return False
        
def piece_names(chessBoard):
    for piece in chessBoard.values():
        if piece in whitePieces or piece in blackPieces:
            return True
        else:
            return False
    

chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
whitePieces = ['wking', 'wqueen', 'wrook', 'wknight', 'wbishop', 'wpawn']
blackPieces = ['bking', 'bqueen', 'brook', 'bknight', 'bbishop', 'bpawn']



print(main(chessBoard))
