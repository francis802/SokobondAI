import controller



valenceElectrons = {"H":1,"O":2,"N":3,"C":4}
atoms = ("H","O","N","C")

class Piece:

    def __init__(self, atom, position, avElectrons):
            self.atom = atom
            self.position = position
            self.avElectrons = avElectrons
            self.connections = []
            self.visited = False
    


class Game:
    def __init__(self, level):
        self.board = level["board"]
        self.player_pos = level["player_pos"]
        self.pieces = self.listPieces()
        self.walls = self.listWalls()
        self.cut_pieces = level["cut_pieces"]
        self.Connections()

    def listPieces(self):
        pieces = []
        for rowIndex, row in enumerate(self.board):
            for colIndex, cell in enumerate(row):
                if cell in atoms:
                    piece = Piece(cell, (rowIndex, colIndex), valenceElectrons[cell])
                    if piece.position != self.player_pos:
                        pieces.append(piece)
                    else:
                        pieces.insert(0, piece)
        return pieces
    
    def listWalls(self):
        walls = []
        for rindex, row in enumerate(self.board):
            for colindex, cell in enumerate(row):
                if cell not in atoms and cell is not None:
                    walls.append((rindex, colindex))
        return walls


    def Connections(self):
        for i in range(len(self.pieces)):
            for j in range(i+1, len(self.pieces)):
                if controller.nearPieces(self.pieces[i], self.pieces[j]) != "":
                    if self.pieces[i].avElectrons > 0 and self.pieces[j].avElectrons > 0:
                        self.pieces[i].connections.append(self.pieces[j])
                        self.pieces[i].avElectrons -= 1
                        self.pieces[j].connections.append(self.pieces[i])
                        self.pieces[j].avElectrons -= 1


class GameState:
    def __init__(self, game):
        self.game = game

    def __eq__(self, other):
        return isinstance(other, GameState) and self.game.pieces == other.game.pieces and self.game.player_pos == other.game.player_pos

    def __hash__(self):
        return hash(str(self.game) + str(self.player_pos))

    def __str__(self):
        return "GameState(" + str(self.game) + ", " + str(self.player_pos) + ")"

    def __repr__(self):
        return str(self)
    
    def valid_gamestate(self, direction):
        return controller.validateMove(self.game, direction)
    
    def move_left(self):
        if self.valid_gamestate("left"):
            return GameState(controller.changeState(self.game, "left"))
    
    def move_right(self):
        if self.valid_gamestate("right"):
            return GameState(controller.changeState(self.game, "right"))
    
    def move_up(self):
        if self.valid_gamestate("up"):
            return GameState(controller.changeState(self.game, "up"))
    
    def move_down(self):
        if self.valid_gamestate("down"):
            return GameState(controller.changeState(self.game, "down"))
    
    def childrenStates(self):
        children = []
        movement_methods = [("left", self.move_left), ("right", self.move_right), ("up", self.move_up), ("down", self.move_down)]
        for move in movement_methods:
            childState = (move[1])()
            if childState is not None:
                children.append(childState)
        return children

    def check_win(self):
        return controller.endGame(self.game)
    

class TreeNode:
    def __init__(self, state, parent=None, heuristicVal=0):
        self.state = state
        self.parent = parent
        self.heuristicVal = heuristicVal
        self.treeDepth()
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def treeDepth(self):
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1
    
    def __eq__(self, other):
        return isinstance(other, TreeNode) and self.state == other.state

    def __hash__(self):
        return hash(str(self.state) + str(self.action))

    def __str__(self):
        return "TreeNode(" + str(self.state) + ", " + str(self.action) + ")"

    def __repr__(self):
        return str(self)