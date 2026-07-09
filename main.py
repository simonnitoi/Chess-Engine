import chess
import chess.pgn

import sys

import GreedFish

import BoardGUI


board = chess.Board()

def printGame(board):
    print(f"---------------\n\n{board}")
    print(str(chess.pgn.Game.from_board(board)))
    print("\n---------------")



# << YOU PLAY IT >>
while True:
    playerSide = input("\"w\" or \"b\" ->")
    if playerSide == "w" or playerSide == "b":
        break

BoardGUI.setBoard(640) # << KEEP IT DIVISIBLE BY 8 >>
BoardGUI.setPosition(board,playerSide)

playerMove = ""
moveOpen = False
if playerSide == "w":
    playerTurn = True
else:
    playerTurn = False

def handle_click(event):
    if board.is_game_over():
        return 
    global playerSide,moveOpen,playerMove,playerTurn
    if playerTurn:
        square = BoardGUI.findSquare(event.x,event.y,playerSide)
        piece = board.piece_at(chess.parse_square(square))
        if piece and (piece.color is board.turn) and (not moveOpen):
            moveOpen = True
            playerMove = square
            BoardGUI.highlightSquare(playerMove,playerSide)
        elif piece and moveOpen and square == playerMove:
            BoardGUI.canvas.delete("highlights")
            moveOpen = False
            playerMove = ""
        elif piece and moveOpen and (piece.color is board.turn):
            BoardGUI.canvas.delete("highlights")
            moveOpen = True
            playerMove = square
            BoardGUI.highlightSquare(playerMove,playerSide)
        elif moveOpen:
            BoardGUI.canvas.delete("highlights")
            playerMove+=square
            if chess.Move.from_uci(playerMove) in board.legal_moves:
                playerMove = chess.Move.from_uci(playerMove)
                board.push(playerMove)
                playerTurn = False
            moveOpen = False
            playerMove = ""
BoardGUI.root.bind("<Button-1>", handle_click)

def play():
    global playerTurn,playerSide

    if board.is_game_over():
        printGame(board)
        return

    if not playerTurn:
        BoardGUI.setPosition(board,playerSide)
        BoardGUI.root.update()
        board.push(GreedFish.getMove(board,4))
        BoardGUI.setPosition(board,playerSide)
        playerTurn = True
    BoardGUI.root.after(round(50),play)


# << IT PLAYS ITSELF >>
# BoardGUI.setBoard(640)
# BoardGUI.setPosition(board,"w")
# def play():
#     if board.is_game_over():
#         printGame(board)
#         return
#     else:
#         board.push(GreedFish.getMove(board,3))
#         BoardGUI.setPosition(board,"w")
#     BoardGUI.root.after(round(50),play)

play()
BoardGUI.root.mainloop()