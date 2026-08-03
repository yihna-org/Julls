import random
board = ['_'] * 9


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
        choice = input("Chose X or O? ").upper()
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
    choice = 0
    while choice not in range(1,10):
        choice = int(input("Pick a position (1-9) - "))
        if choice not in range(1,10):
            print("Sorry, invalid choice!")
        if not space_check(board, choice - 1):
            print("Place been chosen, choose another one.")
        break    
    return choice - 1


def user_move(board, position, marker):
    """Place the player's marker at the given position.
    """
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

def computer_move(board):
    """
    Returns a random position from the available space.
    """

    available = []
    for i in range(9):
        if space_check(board, i):
            available.append(i)
    return random.choice(available)

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

print('Welcome to Tic Tac Toe!')
game_on = True


while game_on:
    board = ["_"] * 9
    player_marker = user_choice()
    computer_marker = "O" if player_marker == "X" else "X"
    display_game(board)
    game_run = True
    while game_run:
        position = position_choice(board)
        user_move(board, position, player_marker)
        display_game(board)
        if win_check(board, player_marker):
            print("Congrats! You won!")
            game_run = False
            break
        if full_board_check(board):
            print('We have a tie^^')
            game_run = False
        print("Computer's turn... ")
        computer_pos = computer_move(board)    
        user_move(board, computer_pos, computer_marker)
        display_game(board)
        if win_check(board, computer_marker):
            print("Cumputer won!")
            game_running = False
            break

        if full_board_check(board):
            print("We have a tie!")
            game_running = False
            break

    game_on = gameon_choice()
