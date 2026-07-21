
def convert_coordinates(coordinate):
    if len(coordinate) != 2:
        raise ValueError("Invalid coordinate format. Please provide a valid coordinate (e.g., 'a1', 'h8').")
    if coordinate[0] < 'a' or coordinate[0] > 'h' or coordinate[1] < '1' or coordinate[1] > '8':
        raise ValueError("Invalid coordinate. Please provide a valid coordinate (e.g., 'a1', 'h8').")
    

    letter = coordinate[0]
    number = coordinate[1]

    col = ord(letter) - ord('a')
    row = 8 - int(number)

    return row, col


