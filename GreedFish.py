import chess
import random

pieceValues = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

def getBoardValue(board):

    if board.is_checkmate():
        if board.turn == chess.BLACK:
            return 9999
        if board.turn == chess.WHITE:
            return -9999
    
    if board.is_game_over():
        return 0

    boardValue = 0
    map = board.piece_map()
    for square, piece in map.items():
        pieceValue = pieceValues[piece.piece_type]
        if piece.color == chess.WHITE:
            boardValue += pieceValue
        else:
            boardValue -= pieceValue
    return boardValue

def minimax(board,depth,alpha=-9999,beta=9999):
    if depth == 0 or board.is_game_over():
        return getBoardValue(board)
    
    if board.turn == chess.WHITE:
        maxEval = -9999
        moves = list(board.legal_moves)
        moves.sort(key=lambda move: board.is_capture(move), reverse=True)
        for move in moves:
            board.push(move)
            eval = minimax(board, depth-1,alpha,beta)
            board.pop()
            maxEval = max(maxEval,eval)
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
        return maxEval
    
    if board.turn == chess.BLACK:
        minEval = 9999
        moves = list(board.legal_moves)
        moves.sort(key=lambda move: board.is_capture(move), reverse=True)
        for move in moves:
            board.push(move)
            eval = minimax(board, depth-1,alpha,beta)
            board.pop()
            minEval = min(minEval,eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        return minEval

def getMove(board,targetDepth):

    moves = list(board.legal_moves)

    moveValues = {move:0 for move in moves}

    for move in moves:
        board.push(move)
        moveValues[move] = minimax(board,targetDepth-1)
        board.pop()

    if board.turn == chess.WHITE:
        maxValue = max(moveValues.values())
        bestMoves = [move for move, moveValue in moveValues.items() if moveValue == maxValue]
        return random.choice(bestMoves)
    
    if board.turn == chess.BLACK:
        minValue = min(moveValues.values())
        bestMoves = [move for move, moveValue in moveValues.items() if moveValue == minValue]
        return random.choice(bestMoves)