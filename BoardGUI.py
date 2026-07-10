import tkinter as tk

from PIL import Image, ImageTk

import chess

root = tk.Tk()

size = 0
squareDim = 0

canvas = tk.Canvas(root)

images = []

def setBoard(dimension):
    global size,squareDim,canvas,root

    size = dimension
    canvas = tk.Canvas(root, width=size, height=size, bg="AntiqueWhite4")
    canvas.pack()

    squareDim = size//8
    for column in range(4):
        for row in range(8):
            canvas.create_rectangle(column*2*squareDim+squareDim*(row%2), row*squareDim, column*2*squareDim+squareDim+squareDim*(row%2), row*squareDim+squareDim, fill="antique white", outline="")

coords = [["a8","b8","c8","d8","e8","f8","g8","h8"],
          ["a7","b7","c7","d7","e7","f7","g7","h7"],
          ["a6","b6","c6","d6","e6","f6","g6","h6"],
          ["a5","b5","c5","d5","e5","f5","g5","h5"],
          ["a4","b4","c4","d4","e4","f4","g4","h4"],
          ["a3","b3","c3","d3","e3","f3","g3","h3"],
          ["a2","b2","c2","d2","e2","f2","g2","h2"],
          ["a1","b1","c1","d1","e1","f1","g1","h1"]]

def findLocation(coord):
    for row in range(len(coords)):
        for coloumn in range(len(coords[row])):
            if coords[row][coloumn] == coord:
                return [row,coloumn]

def highlightSquare(square,side):
    coord = findLocation(square)
    size = squareDim*0.1
    if side == "w":
        x = coord[1]*squareDim+squareDim/2
        y = coord[0]*squareDim+squareDim/2
    else:
        x = (7-coord[1])*squareDim+squareDim/2
        y = (7-coord[0])*squareDim+squareDim/2
    canvas.create_oval(x-size,y-size, x+size,y+size, fill="red", outline="",tags="highlights")


def setPosition(board,side):
    global images,canvas
    images.clear()
    canvas.delete("piece")

    map = board.piece_map()
    for square, piece in map.items():
        coord = findLocation(chess.square_name(square))
        if side == "w":
            x = coord[1]*squareDim
            y = coord[0]*squareDim
        else:
            x = (7-coord[1])*squareDim
            y = (7-coord[0])*squareDim
        if piece.color == chess.WHITE:
            if piece.piece_type == chess.PAWN:
                img = Image.open("assets/whitePawn.png")
            if piece.piece_type == chess.KNIGHT:
                img = Image.open("assets/whiteKnight.png")
            if piece.piece_type == chess.BISHOP:
                img = Image.open("assets/whiteBishop.png")
            if piece.piece_type == chess.ROOK:
                img = Image.open("assets/whiteRook.png")
            if piece.piece_type == chess.QUEEN:
                img = Image.open("assets/whiteQueen.png")
            if piece.piece_type == chess.KING:
                img = Image.open("assets/whiteKing.png")
        else:
            if piece.piece_type == chess.PAWN:
                img = Image.open("assets/blackPawn.png")
            if piece.piece_type == chess.KNIGHT:
                img = Image.open("assets/blackKnight.png")
            if piece.piece_type == chess.BISHOP:
                img = Image.open("assets/blackBishop.png")
            if piece.piece_type == chess.ROOK:
                img = Image.open("assets/blackRook.png")
            if piece.piece_type == chess.QUEEN:
                img = Image.open("assets/blackQueen.png")
            if piece.piece_type == chess.KING:
                img = Image.open("assets/blackKing.png")
        img = img.resize((squareDim,squareDim), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)

        images.append(tk_img) # this is just so that the images aren't erased from cache
        canvas.create_image(x, y, image=tk_img, anchor=tk.NW, tags="piece")

def findSquare(x,y,side):
    row = 0
    column = 0
    for i in range(8):
        if (i+1)*squareDim < x:
            column +=1
        if (i+1)*squareDim < y:
            row +=1
    if side == "b":
        row = 7-row
        column = 7-column
    return coords[row][column]