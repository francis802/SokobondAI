import controller



valenceElectrons = {"H":1,"O":2}
atoms = ("H","O")

class Piece:

    def __init__(self, color, position, avElectrons):
            self.color = color
            self.position = position
            self.avElectrons = avElectrons
            self.connections = []
    


class Game:
    def __init__(self, board, player_pos):
        self.board = board
        self.player_pos = player_pos
        self.pieces = self.listPieces()
        self.walls = self.listWalls()
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


 
