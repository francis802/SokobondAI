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
    else:
        initSearch(game)
    
    pivot = game.pieces[0]
    new_poss = [(pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])]
    pivot.position = (pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])
    pivot.visited = True
    moveAjacentPiece(game, direction, pivot, new_poss)
    
    return

def moveAjacentPiece(game, direction, pivot, new_poss):
    for piece in pivot.connections:
        new_poss.append((piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1]))
        piece.position = (piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1])
        piece.visited = True
    
    for piece in game.pieces:
        if piece.position in new_poss and piece != pivot and piece not in pivot.connections and not piece.visited:
            new_poss.append((piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1]))
            piece.position = (piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1])
            piece.visited = True
            moveAjacentPiece(game, direction, piece, new_poss)
    return



def validateMove(game, direction):
    pivot = game.pieces[0]
    initSearch(game)
    game.pieces[0].visited = True
    return checkMovePiece(pivot, game, direction)

def checkMovePiece(pivot, game, direction):
    if(wallCollision(pivot, game, direction)):
        return "stop"
    for otherPiece in game.pieces:
        if (nearPieces(pivot, otherPiece) == direction and otherPiece not in pivot.connections):
            print("Other piece: ", otherPiece.position)
            result = checkMovePiece(otherPiece, game, direction)
            if result == "stop":
                return "stop"

    for connectedPiece in pivot.connections:
        if not connectedPiece.visited:
            connectedPiece.visited = True
            result = checkMovePiece(connectedPiece, game, direction)
            if result == "stop":
                return "stop"
    return "move"

def wallCollision(pivot, game, direction):
    new_move = (pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])
    print("Move: ", new_move)
    if(new_move in game.walls):
        return True
    return False

def initSearch(game):
    for piece in game.pieces:
        piece.visited = False
    return

def nearPieces(piece1, piece2):
    if piece1.position[1] == piece2.position[1]:
        if (piece1.position[0] + 1 == piece2.position[0]):
            return "down"
        if (piece1.position[0] - 1 == piece2.position[0]):
            return "up"
    if piece1.position[0] == piece2.position[0]:
        if (piece1.position[1] + 1 == piece2.position[1]):
            return "right"
        if (piece1.position[1] - 1 == piece2.position[1]):
            return "left"
    return ""



