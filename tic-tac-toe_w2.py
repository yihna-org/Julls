import random

board = ["_"] * 9
name1 = "1 Player"
name2 = "2 Player"


def display_game(board):
    """Print the current state of the tic-tac-toe board.

    Parameters - board : list
    Lists of three elements representing each row of the board.
    """
    print("Here is the current board:")
    print("| " + " | ".join(board[0:3]) + " |")
    print("| " + " | ".join(board[3:6]) + " |")
    print("| " + " | ".join(board[6:9]) + " |")


def user_choice():
    """Ask the player to choose a marker.

    Keeps prompting until the input is either 'X' or 'O'.
    """
    choice = "wrong"
    while choice not in ["X", "O"]:
        choice = input(f"{name1} choses X or O? ").upper()
        if choice not in ["X", "O"]:
            print("Sorry, invalid choice!")
    return choice


def space_check(board, position):
    """
    Checks if the position is available.

    Returns True if the position is available and False if it is not.
    """

    return board[position] == "_"


def position_choice(board):
    """Ask the player to choose a position.

    Keeps prompting until the input is 1-9. The result is
    converted to a zero-based list index before being returned.
    """
    choice = "wrong"

    while True:
        choice = input("Pick a position (1-9) - ")
        if choice.isdigit() == False:
            print("Sorry, invalid format! Expected a digit (1-9)")
        else:
            choice = int(choice)
            if choice not in range(1, 10):
                print("Sorry, invalid range! Pick a number within the range (1-9)")
            elif not space_check(board, choice - 1):
                print("Place's been chosen, choose another one.")
            else:
                return choice - 1


def user_move(board, position, marker):
    """Place the player's marker at the given position."""
    board[position] = marker


def full_board_check(board):
    """
    Checks if the board is full.

    Returns True if all position is not available.
    """
    return "_" not in board


def win_check(board, mark):
    """
    Checks whether there are any winning combinations in the game.

    Returns True if any combination is a winner.
    """

    win_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(
        board[a] == mark and board[b] == mark and board[c] == mark
        for a, b, c in win_combinations
    )


def choose_first():
    """Randomly selects which of the two players goes first.

    Returns:
        str: (name1 or name2).
    """
    if random.randint(0, 1) == 0:
        return name1
    else:
        return name2


def gameon_choice():
    """Ask the player whether to continue the game.

    Keeps prompting until the input is 'Y' or 'N'.
    """

    choice = "wrong"
    while choice not in ["Y", "N"]:
        choice = input("Continue game (Y or N)? ").upper()
        if choice not in ["Y", "N"]:
            print("Sorry, invalid choice!")
    if choice == "Y":
        return True
    else:
        return False


print("Welcome to Tic Tac Toe!")
game_on = True
name1 = input("1 Player name: ")
name2 = input("2 Player name: ")

while game_on:
    board = ["_"] * 9
    f_player = user_choice()
    s_player = "O" if f_player == "X" else "X"
    turn = choose_first()
    print(f"{turn} will go first.")
    game_run = True
    display_game(board)
    while game_run:
        if turn == name1:
            print(f"{name1} turn")
            position = position_choice(board)
            user_move(board, position, f_player)
            display_game(board)
            if win_check(board, f_player):
                print(f"Congrats! {name1} won!")
                game_run = False
                break
            if full_board_check(board):
                print("We have a tie^^")
                game_run = False
            else:
                turn = name2
        else:
            print(f"{name2} turn")
            s_player_pos = position_choice(board)
            user_move(board, s_player_pos, s_player)
            display_game(board)
            if win_check(board, s_player):
                print(f"Congrats!{name2} won!")
                game_run = False
                break

            if full_board_check(board):
                print("We have a tie!")
                game_run = False
                break
            else:
                turn = name1

    game_on = gameon_choice()
