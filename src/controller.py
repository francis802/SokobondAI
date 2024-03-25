import pygame
import view
import model
import copy
import algorythms


# ATENTION: The y axis is turned upside down, so to go up you have to subtract 1, and add 1 to go down!!!
moves = {"right": (0,1), "left": (0,-1), "up": (-1,0), "down": (1,0)}

def movePiece(game, direction):
    if direction not in moves.keys():
        raise ValueError("Invalid direction")
    
    if validateMove(game, direction) == "stop":
        return
    else:
        algorythms.initSearch(game)
    
    pivot = game.pieces[0]
    new_poss = [(pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])]
    pivot.position = (pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])
    pivot.visited = True
    moveAjacentPiece(game, direction, pivot, new_poss)
    
    newConnections(game)

    for piece in game.pieces:
        print(piece.atom, end=": ")
        print(piece.position)
        print("Connections:", end=" ")
        print(piece.connections)
        print("Available Electrons:", end=" ")
        print(piece.avElectrons)
        print("-----------------")

    measure = algorythms.proximityMeasure(game)
    print("Proximity Measure: ", measure)
    print("Pivot: ", pivot.position)

    return

def newConnections(game):
    for piece in game.pieces:
        for possibleConnection in game.pieces:
            if piece != possibleConnection and possibleConnection not in piece.connections and (nearPieces(piece, possibleConnection) != "") and piece.avElectrons > 0 and possibleConnection.avElectrons > 0:
                piece.connections.append(possibleConnection)
                piece.avElectrons -= 1
                possibleConnection.connections.append(piece)
                possibleConnection.avElectrons -= 1
    return

def moveAjacentPiece(game, direction, pivot, new_poss):
    for piece in pivot.connections:
        if not piece.visited:
            new_poss.append((piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1]))
            piece.position = (piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1])
            piece.visited = True
            moveAjacentPiece(game, direction, piece, new_poss)
    
    for piece in game.pieces:
        if piece.position in new_poss and piece != pivot and piece not in pivot.connections and not piece.visited:
            new_poss.append((piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1]))
            piece.position = (piece.position[0] + moves[direction][0], piece.position[1] + moves[direction][1])
            piece.visited = True
            moveAjacentPiece(game, direction, piece, new_poss)
    return



def validateMove(game, direction):
    pivot = game.pieces[0]
    algorythms.initSearch(game)
    game.pieces[0].visited = True
    prev_pieces_state = copy.deepcopy(game.pieces)
    if checkMovePiece(pivot, game, direction) == "stop":
        game.pieces = prev_pieces_state
        return "stop"
    return "move"

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
            if not checkDotCrossing(pivot, connectedPiece, direction, game.cut_pieces):
                connectedPiece.visited = True
                result = checkMovePiece(connectedPiece, game, direction)
                if result == "stop":
                    return "stop"
            else:
                pivot.connections.remove(connectedPiece)
                pivot.avElectrons += 1
                connectedPiece.connections.remove(pivot)
                connectedPiece.avElectrons += 1
    return "move"

def wallCollision(pivot, game, direction):
    new_move = (pivot.position[0] + moves[direction][0], pivot.position[1] + moves[direction][1])
    print("Move: ", new_move)
    if(new_move in game.walls):
        print("Wall collision")
        return True
    return False

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

def checkDotCrossing(pivot, connectPiece, direction, dotsArray):
    connectedDir = nearPieces(pivot, connectPiece)

    # Tuple with the expected direction of the dot
    # The first element is the direction of the connected piece relative to the pivot
    # The second element is the direction chosen by the player
    directions = {
        ("right", "up"): (0, 1),
        ("right", "down"): (1, 1),
        ("left", "up"): (0, 0),
        ("left", "down"): (1, 0),
        ("up", "right"): (0, 1),
        ("up", "left"): (0, 0),
        ("down", "right"): (1, 1),
        ("down", "left"): (1, 0),
    }

    for dot in dotsArray:
        maxDotDist = max(abs(dot[0] - pivot.position[0]), abs(dot[1] - pivot.position[1]))
        if maxDotDist > 1 or (connectedDir, direction) not in directions.keys():
            continue
        expected_position = (pivot.position[0] + directions[(connectedDir, direction)][0], pivot.position[1] + directions[(connectedDir, direction)][1])
        if dot == expected_position:
            return True

    return False


def endGame(game):
    algorythms.initSearch(game)
    algorythms.dfs(game.pieces[0])
    for piece in game.pieces:
        if not piece.visited or piece.avElectrons > 0:
            return False
    return True

