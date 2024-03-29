import controller
import copy



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
        return isinstance(other, GameState) and self.comparePieces(other)

    def comparePieces(self, other):
        for i in range(len(self.game.pieces)):
            if self.game.pieces[i].atom != other.game.pieces[i].atom or self.game.pieces[i].position != other.game.pieces[i].position or self.game.pieces[i].avElectrons != other.game.pieces[i].avElectrons:
                return False
            if len(self.game.pieces[i].connections) != len(other.game.pieces[i].connections):
                return False
            for j in range(len(self.game.pieces[i].connections)):
                if self.game.pieces[i].connections[j].position != other.game.pieces[i].connections[j].position:
                    return False
        return True

    def __hash__(self):
        return hash(str(self.game.pieces))

    def __str__(self):
        return "GameState(" + str(self.game.pieces) + ")"

    def __repr__(self):
        return str(self)
    
    def valid_gamestate(self, direction):
        return controller.validateMove(self.game, direction)
    
    def move_left(self):
        if self.valid_gamestate("left"):
            state = GameState(controller.changeState(copy.deepcopy(self.game), "left"))
            if not controller.impossible_solution(state.game):
                return state
    
    def move_right(self):
        if self.valid_gamestate("right"):
            state = GameState(controller.changeState(copy.deepcopy(self.game), "right"))
            if not controller.impossible_solution(state.game):
                return state
    
    def move_up(self):
        if self.valid_gamestate("up"):
            state = GameState(controller.changeState(copy.deepcopy(self.game), "up"))
            if not controller.impossible_solution(state.game):
                return state
    
    def move_down(self):
        if self.valid_gamestate("down"):
            state = GameState(controller.changeState(copy.deepcopy(self.game), "down"))
            if not controller.impossible_solution(state.game):
                return state
    
    def childrenStates(self):
        children = []
        movement_methods = [("left", self.move_left), ("right", self.move_right), ("up", self.move_up), ("down", self.move_down)]
        for move in movement_methods:
            childState = (move[1])()
            if childState is not None:
                children.append((move[0],childState))
        return children

    def check_win(self):
        return controller.endGame(self.game)
    

class TreeNode:
    def __init__(self, state, prev_move=None, parent=None, heuristicVal=0):
        self.state = state
        self.prev_move = prev_move
        self.parent = parent
        self.heuristicVal = heuristicVal
        self.treeDepth()
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
        self.treeDepth()

    def treeDepth(self):
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1
    
    def __eq__(self, other):
        return isinstance(other, TreeNode) and self.state == other.state

    def __hash__(self):
        return hash(str(self.state) + str(self.depth))

    def __str__(self):
        return "TreeNode(" + str(self.state) + ", " + str(self.depth) + ")"

    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        return self.heuristicVal < other.heuristicVal
    
    def print_solution(self):
        stack = []
        current = self
        while current is not None:
            stack.append(current.prev_move)
            current = current.parent
        stack.pop() # First element of stack is None (root)
        while len(stack)>1:
            print(stack.pop(), " -> ", end="")
        print(stack.pop())
        return