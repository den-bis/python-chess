from board import Board
from pieces import Piece, Pawn, Rock, Knight, Bishop, Queen, King
from utils import  convert_coordinates

game_board = Board()

pawn1 = Pawn("White")
pawn2 = Pawn("Black")
pawn3 = Pawn("White")
pawn4 = Pawn("Black")   
pawn5 = Pawn("White")
pawn6 = Pawn("Black")
pawn7 = Pawn("White")
pawn8 = Pawn("Black")
pawn9 = Pawn("White")
pawn10 = Pawn("Black")
pawn11 = Pawn("White")
pawn12 = Pawn("Black")  
pawn13 = Pawn("White")
pawn14 = Pawn("Black")
pawn15 = Pawn("White")
pawn16 = Pawn("Black")

game_board.place_piece(pawn1, "e2")
game_board.place_piece(pawn2, "e7")
game_board.place_piece(pawn3, "d2")
game_board.place_piece(pawn4, "d7")
game_board.place_piece(pawn5, "f2")
game_board.place_piece(pawn6, "f7")
game_board.place_piece(pawn7, "g2")
game_board.place_piece(pawn8, "g7")
game_board.place_piece(pawn9, "h2")
game_board.place_piece(pawn10, "h7")
game_board.place_piece(pawn11, "a2")
game_board.place_piece(pawn12, "a7")
game_board.place_piece(pawn13, "b2")
game_board.place_piece(pawn14, "b7")
game_board.place_piece(pawn15, "c2")
game_board.place_piece(pawn16, "c7")


game_board.display()

# piece1 = str(input())

# try:
#     result = convert_coordinates(piece1)
# except ValueError as e:
#     print(e)




# coordinates_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
# coordinates_numbers = [8, 7, 6, 5, 4, 3, 2, 1]

# print(coordinates_numbers)
# print(coordinates_letters)
