import pygame
import view
import model


# ATENTION: The y axis is turned upside down, so to go up you have to subtract 1, and add 1 to go down!!!
moves = {"right": (1,0), "left": (-1,0), "up": (0,-1), "down": (0,1)}

def movePiece(game, direction):
    if direction == "up":
        
    elif direction == "down":
        
    elif direction == "left":

    elif direction == "right":
        
    else:
        raise ValueError("Invalid direction")


def validateMove(game, direction):
    pivot = game.pieces[0]
    if not pivot.connections:
        for otherPiece in game.pieces:
            if (otherPiece not in pivot.connected) and (nearPieces(otherPiece, pivot) != direction):
                new_move = (pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])
                if(new_move not in game.walls):
                    return "move"
                else:
                    return "stop"
            elif (otherPiece not in pivot.connected) and (nearPieces(otherPiece, pivot) == direction):
                a = 0
    else:
        a = 0

def checkMovePiece(): # To implement
    return True

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



