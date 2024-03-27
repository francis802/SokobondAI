from model import TreeNode, GameState, Game
from collections import deque
import heapq

def initSearch(game):
    for piece in game.pieces:
        piece.visited = False
    return

def depth_search(piece):
    piece.visited = True
    for connectedPiece in piece.connections:
        if not connectedPiece.visited:
            depth_search(connectedPiece)
    return

def evaluation(game):
    initSearch(game)
    molecules = 0
    for piece in game.pieces:
        if not piece.visited:
            molecules += 1
            depth_search(piece)
    
    totalElectrons = 0
    for piece in game.pieces:
        totalElectrons += piece.avElectrons
    
    return molecules * (totalElectrons + 1)


def distance(piece1, piece2):
    return abs(piece1.position[0] - piece2.position[0]) + abs(piece1.position[1] - piece2.position[1])

def noWallBetween(game, piece1, piece2):
    # print("Checking: ", piece1.position, piece2.position)
    if piece1.position[0] == piece2.position[0]:
        for i in range(min(piece1.position[1], piece2.position[1]), max(piece1.position[1], piece2.position[1])):
            print("Checking: ", (piece1.position[0], i))
            if (piece1.position[0], i) in game.walls:
                return False
    if piece1.position[1] == piece2.position[1]:
        for i in range(min(piece1.position[0], piece2.position[0]), max(piece1.position[0], piece2.position[0])):
            print("Checking: ", (i, piece1.position[1]))
            if (i, piece1.position[1]) in game.walls:
                return False
    # print("No wall between")
    # print ("------------------------------------------")
    return True


# This function will return the minimum distance between the molecule and the nearst atom
def proximityMeasure(game):
    # See in connections of the pivot atom whish has the minimum distance to some atom
    minDistance = 100000000
    pivot = game.pieces[0]
    molecule = pivot
    near = pivot

    for piece in game.pieces:
            if piece != pivot and noWallBetween(game, pivot, piece) and piece not in pivot.connections and pivot.avElectrons > 0:
                temp = min(minDistance, distance(pivot, piece))
                if temp < minDistance:
                    minDistance = temp
                    near = piece


    if len(pivot.connections) != 0:    
        for piece1 in pivot.connections:
            for piece2 in game.pieces:
                if piece2 != pivot and piece2 not in pivot.connections and noWallBetween(game, piece1, piece2) and piece1.avElectrons > 0:
                    temp = min(minDistance, distance(piece1, piece2))
                    if temp < minDistance:
                        minDistance = temp
                        near = piece2
                        molecule = piece1
    
    print("Molecule: ", molecule.position)
    print("Near: ", near.position)
    
    return minDistance - 1


# Algorithm for GameState

def BFS(game: Game):
    visited = []
    root = TreeNode(GameState(game))
    queue = deque([root])

    while queue:
        node = queue.popleft()  
        node.treeDepth()
        if node.state.check_win():
            return node
        
        if node not in visited:
            visited.append(node)
            for state in node.state.childrenStates():
                leaf = TreeNode(state[1])
                leaf.prev_move = state[0]
                node.add_child(leaf)
                queue.append(leaf)
    return None

def DFS(game: Game):
    visited = []
    root = TreeNode(GameState(game))
    stack = [root]

    while stack:
        node = stack.pop()  
        node.treeDepth()
        if node.state.check_win():
            return node
        
        if node not in visited:
            visited.append(node)
            for state in node.state.childrenStates():
                leaf = TreeNode(state[1])
                leaf.prev_move = state[0]
                node.add_child(leaf)
                stack.append(leaf)
    return None