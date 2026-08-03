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


def row_choice():
    """Ask the player to choose a row.

    Keeps prompting until the input is '1', '2', or '3'.
    """

    choice = "wrong"
    while choice not in ["1", "2", "3"]:
        choice = input("Pick a row (1,2,3) - ")
        if choice not in ["1", "2", "3"]:
            print("Sorry, invalid choice!")
    return choice


def position_choice():
    """Ask the player to choose a position within a row.

    Keeps prompting until the input is 1, 2, or 3. The result is
    converted to a zero-based list index before being returned.
    """
    choice = 0
    while choice not in [1, 2, 3]:
        choice = int(input("Pick a position (1,2,3) - "))
        if choice not in [1, 2, 3]:
            print("Sorry, invalid choice!")
    return choice - 1  # 


def user_move(row, position, marker):
    """Place the player's marker at the given position in a row.
    """
    row[position] = marker


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


game_on = True
rows = {"1": row1, "2": row2, "3": row3}

while game_on:
    display_game(row1, row2, row3)
    marker = user_choice()
    row_num = row_choice()
    position = position_choice()
    user_move(rows[row_num], position, marker)
    game_on = gameon_choice()
