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


 
