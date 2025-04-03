class TTT(object):
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.turn_player = "X"
        self.turns_played = 0

    def __str__(self):
        rows = self.get_rows()
        result = ""
        for i, row in enumerate(rows):
            result += f"{row[0]}|{row[1]}|{row[2]}\n"
            if i < 2:  # Add separator line except after the last row
                result += "-+-+-\n"
        return result

    def get_rows(self) -> list:
        return [self.board[:3], self.board[3:6], self.board[6:]]

    def get_columns(self) -> list:
        col_0 = [self.board[0], self.board[3], self.board[6]]
        col_1 = [self.board[1], self.board[4], self.board[7]]
        col_2 = [self.board[2], self.board[5], self.board[8]]
        return [col_0, col_1, col_2]

    def get_diagonals(self) -> list:
        dia_0 = [self.board[0], self.board[4], self.board[8]]
        dia_1 = [self.board[2], self.board[4], self.board[6]]
        return [dia_0, dia_1]

    def is_valid_move(self, move: int) -> bool:
        # validate input
        if not 0 <= move <= 8:
            print("\n")
            print("Invalid move: position out of bounds.\n")
            return False

        # row and column are in bounds
        position = self.board[move]

        # position has already been played
        if position == "X" or position == "O":
            print("\n")
            print("Invalid move: position has already been played.\n")
            return False

        return True

    def is_game_ended(self) -> bool:
        """
        checks if one of the win conditions has been met:
        - one row is full of turn_player or
        - one column is full of turn_player or
        - one diagonal is full of turn_player
        """
        def is_all_same(list: list) -> bool:
            return len(set(list)) <= 1

        def check_win_condition(direction_fn) -> bool:
            for direction in direction_fn():
                if is_all_same(direction) and " " not in direction:
                    return True
            return False

        row__win = check_win_condition(self.get_rows) 
        column_win = check_win_condition(self.get_columns)
        diagonal_win = check_win_condition(self.get_diagonals)

        return row__win or column_win or diagonal_win

if __name__ == "__main__":
    game = TTT()
    while True and game.turns_played != 9:
        # print turn player
        print("\n")
        print(f"{game.turn_player}'s turn. \n")

        # print board
        print(game)

        # prompt player for move
        move = int(input("Where do you want to play? (number): "))

        # play
        if game.is_valid_move(move):
            game.board[move] = game.turn_player
            game.turns_played += 1
        
            # check if game has ended
            if game.is_game_ended():
                break

            # change turn player
            if game.turn_player == "X":
                game.turn_player = "O"
            else:
                game.turn_player = "X"

    print("\n")
    print(game)

    if game.turns_played == 9:
        print("Game ended in a draw.")
    else:
        print(f"Congratulations {game.turn_player} you have won!\n")
