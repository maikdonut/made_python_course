class TicTacGame:
    """
    Console tictac game
    """

    def __init__(self):
        self.board = list(range(1, 10))

    def start_game(self):
        print("The game has begun")
        self.show_board()
        print("First player, choose X or O:")
        first, second = validate_input()
        self.game_processing(first, second)

    def show_board(self):
        print("-------------")
        for i in range(3):
            print(
                "|",
                self.board[0 + i * 3],
                "|",
                self.board[1 + i * 3],
                "|",
                self.board[2 + i * 3],
                "|",
            )
            print("-------------")

    def game_processing(self, first, second):
        print(f"First player plays {first}, second player plays {second}")
        cells = self.board.copy()
        while True:
            print(f"First player ({first}), your turn")
            print(f"Choose one of the next cells: {cells}")
            step = step_processing(cells)
            cells.remove(step)
            self.board[step - 1] = first
            self.show_board()
            if self.check_winner():
                print("First player wins")
                return
            if len(cells) == 0:
                print("Draw")
                return
            print(f"Second player ({second}), your turn")
            print(f"Choose one of the next cells: {cells}")
            step = step_processing(cells)
            cells.remove(step)
            self.board[step - 1] = second
            self.show_board()
            if self.check_winner():
                print("Second player wins")
                return

    def check_rows(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                return True
        return False

    def check_columns(self):
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                return True
        return False

    def check_diagonals(self):
        if self.board[0] == self.board[4] == self.board[8]:
            return True
        if self.board[2] == self.board[4] == self.board[6]:
            return True
        return False

    def check_winner(self):
        if self.check_rows() or self.check_columns() or self.check_diagonals():
            return True
        return False


def validate_input():
    while True:
        first = input()
        if first in ["X", "O"]:
            break
        print("Wrong input. Please, enter X or O:")
    second = "O" if first == "X" else "X"
    return first, second


def step_processing(cells):
    while True:
        step = input("Num of cell: ")
        if step.isdigit() and int(step) in cells:
            step = int(step)
            break
        print("Wrong input. Please, enter one of the next number:", cells)
    return step


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
