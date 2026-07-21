from utils import  convert_coordinates

class Board:
    def __init__(self):
        self.board = [[None]*8 for _ in range(8)]

    def place_piece(self, piece, position):
        row, col = convert_coordinates(position)
        self.board[row][col] = piece


    def display(self):
        i = 8
        for  i, row in enumerate(self.board):
            print(8 - i, " ", end="") 
            for cell in row:
                if cell is None:
                    print(".  ",end="")
                else:
                    print(cell.symbol, end="") 
            print("")  # Move to the next line after printing a row
            
            
        print("   a  b  c  d  e  f  g  h")


        # row = ["a", "b",  "c",  "d", "e", "f",  "g",  "h"]
        # line = [1, 2, 3, 4, 5, 6, 7, 8]


