import chess
import chess.pgn

from tkinter import simpledialog

import sys

import GreedFish

import BoardGUI


board = chess.Board()

def printGame(board):
    print(f"---------------\n\n{board}")
    print(str(chess.pgn.Game.from_board(board)))
    print("\n---------------")



# << YOU PLAY IT >>
BoardGUI.setBoard(640) # << KEEP IT DIVISIBLE BY 8 >>

while True:
    playerSide = simpledialog.askstring("Pick a Side","\"w\" or \"b\":",parent=BoardGUI.root)
    if playerSide == None:
        sys.exit(0)
    if playerSide == "w" or playerSide == "b":
        break

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
            elif chess.Move.from_uci(playerMove+"q") in board.legal_moves:
                promo = simpledialog.askstring("Promotion","Promote to (\"q\",\"r\",\"b\",\"n\"):",parent=BoardGUI.root)
                if not promo or promo not in ["q","r","b","n"]:
                    pass
                else:
                    playerMove = chess.Move.from_uci(playerMove+promo)
                    board.push(playerMove)
                    playerTurn = False
            moveOpen = False
            playerMove = ""
BoardGUI.root.bind("<Button-1>", handle_click)

def play():
    global playerTurn,playerSide

    if not playerTurn:
        BoardGUI.setPosition(board,playerSide)
        BoardGUI.root.update()
        if board.is_game_over():
            printGame(board)
            return
        board.push(GreedFish.getMove(board,5))
        BoardGUI.setPosition(board,playerSide)
        if board.is_game_over():
            printGame(board)
            return
        playerTurn = True
    BoardGUI.root.after(round(50),play)


# << IT PLAYS ITSELF >>
# BoardGUI.setBoard(640) # << KEEP IT DIVISIBLE BY 8 >>
# BoardGUI.setPosition(board,"w")
# def play():
#     if board.is_game_over():
#         printGame(board)
#         return
#     else:
#         board.push(GreedFish.getMove(board,5))
#         BoardGUI.setPosition(board,"w")
#     BoardGUI.root.after(round(50),play)

play()
BoardGUI.root.mainloop()