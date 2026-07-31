row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]


def display_game(row1, row2, row3):
    print("Here is the current board:")
    print("| " + " | ".join(row1) + " |")
    print("| " + " | ".join(row2) + " |")
    print("| " + " | ".join(row3) + " |")


def user_choice():
    choice = "wrong"
    while choice not in ["X", "O"]:
        choice = input("Chose X or O? ").upper()
        if choice not in ["X", "O"]:
            print("Sorry, invalid choice!")
    return choice


def row_choice():
    choice = "wrong"
    while choice not in ["1", "2", "3"]:
        choice = input("Pick a row (1,2,3) - ")
        if choice not in ["1", "2", "3"]:
            print("Sorry, invalid choice!")
    return choice


def position_choice():
    choice = 0
    while choice not in [1, 2, 3]:
        choice = int(input("Pick a position (1,2,3) - "))
        if choice not in [1, 2, 3]:
            print("Sorry, invalid choice!")
    return choice - 1  # переводимо 1,2,3 у індекс списку 0,1,2


def user_move(row, position, marker):
    row[position] = marker


def gameon_choice():
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
