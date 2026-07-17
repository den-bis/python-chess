class Board:
    def __init__(self):
        self.board = [
            ["."] * 8 for _ in range(8)
        ]

    def display(self):
        for row in self.board:
            print(" ".join(row))