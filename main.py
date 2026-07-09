import chess
import chess.pgn

import GreedFish

board = chess.Board()

# << YOU PLAY IT >>
while True:
    playerSide = input("\"w\" or \"b\" ->")
    if playerSide == "w" or playerSide == "b":
        break

if playerSide == "b":
    board.push(GreedFish.getMove(board,4))

while not board.is_game_over():
    print(f"---------------\n\n{board}\n\nLegal Moves: {str(board.legal_moves).split("(")[1].split(")")[0]}\n")
    playerMove = input("Your Move ->")
    while True:
        try:
            board.push_san(playerMove)
            break
        except:
            playerMove = input("Error! Your Move ->")
    if not board.is_game_over():
        board.push(GreedFish.getMove(board,4))
    print("\n---------------")



# << IT PLAYS ITSELF >>
# while not board.is_game_over():
#     board.push(GreedFish.getMove(board,3))



print(f"---------------\n\n{board}")
print(str(chess.pgn.Game.from_board(board)))
print("\n---------------")