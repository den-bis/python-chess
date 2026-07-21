class Piece:
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    symbol = "P  "
    pass

class Rock(Piece):
    symbol = "R  "
    pass

class Knight(Piece):
    symbol = "N  "
    pass

class Bishop(Piece):
    symbol = "B  "
    pass

class Queen(Piece):
    symbol = "Q  "
    pass

class King(Piece):
    symbol = "K  "
    pass
