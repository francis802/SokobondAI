import pygame
import view
import model


# ATENTION: The y axis is turned upside down, so to go up you have to subtract 1, and add 1 to go down!!!
moves = {"right": (0,1), "left": (0,-1), "up": (-1,0), "down": (1,0)}

def movePiece(game, direction):
    if direction not in moves.keys():
        raise ValueError("Invalid direction")
    
    if validateMove(game, direction) == "stop":
        return
    
    pivot = game.pieces[0]
    new_poss = [(pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])]
    pivot.position = (pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])
    for piece in pivot.connections:
        new_poss.append((piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1]))
        piece.position = (piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1])
    
    for piece in game.pieces:
        if piece.position in new_poss and piece != pivot and piece not in pivot.connections:
            new_poss.append((piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1]))
            piece.position = (piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1])
    
    return



def validateMove(game, direction):
    pivot = game.pieces[0]
    return checkMovePiece(pivot, game, direction)

def checkMovePiece(pivot, game, direction): # To implement
    new_move = (pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])
    if(new_move in game.walls):
        return "stop"
    if not pivot.connections:
        for otherPiece in game.pieces:
            if (nearPieces(otherPiece, pivot) == direction):
                result = checkMovePiece(otherPiece, game, direction)
                if result == "stop":
                    return "stop"
        return "move"
    else:
        for connectedPiece in pivot.connections:
            for otherPiece in game.pieces:
                if (otherPiece not in pivot.connections):
                    if (nearPieces(connectedPiece, otherPiece) == direction):
                        result = checkMovePiece(otherPiece, game, direction)
                        if result == "stop":
                            return "stop"
        return "move"

def nearPieces(piece1, piece2):
    if piece1.position[0] == piece2.position[0]:
        if (piece1.position[1] == piece2.position[1] + 1):
            return "down"
        if (piece1.position[1] == piece2.position[1] - 1):
            return "up"
    if piece1.position[1] == piece2.position[1]:
        if (piece1.position[0] == piece2.position[0] + 1):
            return "right"
        if (piece1.position[0] == piece2.position[0] - 1):
            return "left"
    return ""



