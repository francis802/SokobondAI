
def initSearch(game):
    for piece in game.pieces:
        piece.visited = False
    return

def dfs(piece):
    piece.visited = True
    for connectedPiece in piece.connections:
        if not connectedPiece.visited:
            dfs(connectedPiece)
    return

def evaluation(game):
    initSearch(game)
    molecules = 0
    for piece in game.pieces:
        if not piece.visited:
            molecules += 1
            dfs(piece)
    
    totalElectrons = 0
    for piece in game.pieces:
        totalElectrons += piece.avElectrons
    
    return molecules * (totalElectrons + 1)