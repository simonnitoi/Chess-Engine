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

def quietSearch(board,qDepth,alpha=-9999,beta=9999):
    captures = [move for move in board.legal_moves if board.is_capture(move)]

    if len(captures) == 0 or qDepth == 0:
        return getBoardValue(board)
    
    if board.turn == chess.WHITE:
        maxEval = getBoardValue(board)
        for capture in captures:
            board.push(capture)
            eval = quietSearch(board, qDepth-1, alpha,beta)
            board.pop()
            maxEval = max(maxEval,eval)
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
        return maxEval
    
    if board.turn == chess.BLACK:
        minEval = getBoardValue(board)
        for capture in captures:
            board.push(capture)
            eval = quietSearch(board, qDepth-1, alpha,beta)
            board.pop()
            minEval = min(minEval,eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        return minEval

def minimax(board,depth,qDepth,alpha,beta):
    if board.is_game_over():
        return getBoardValue(board)

    if depth == 0:
        return quietSearch(board,qDepth,alpha,beta)
    
    if board.turn == chess.WHITE:
        maxEval = -9999
        moves = list(board.legal_moves)
        moves.sort(key=lambda move: board.is_capture(move), reverse=True)
        for move in moves:
            board.push(move)
            eval = minimax(board, depth-1, qDepth, alpha,beta)
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
            eval = minimax(board, depth-1, qDepth, alpha,beta)
            board.pop()
            minEval = min(minEval,eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        return minEval

def getMove(board,targetDepth,qDepth):

    moves = list(board.legal_moves)
    random.shuffle(moves)
    moves.sort(key=lambda move: board.is_capture(move), reverse=True)

    alpha=-9999
    beta=9999

    if board.turn == chess.WHITE:
        bestMove = moves[0]
        for move in moves:
            board.push(move)
            eval = minimax(board,targetDepth-1,qDepth,alpha,beta)
            board.pop()
            if eval > alpha:
                bestMove = move
                alpha = eval
        return bestMove
    
    if board.turn == chess.BLACK:
        bestMove = moves[0]
        for move in moves:
            board.push(move)
            eval = minimax(board,targetDepth-1,qDepth,alpha,beta)
            board.pop()
            if eval < beta:
                bestMove = move
                beta = eval
        return bestMove