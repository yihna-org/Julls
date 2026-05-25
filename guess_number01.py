from random import randint as num

count = 10

inp_box = int(input(f"Guess the number (1-100). You have {count} guesses! "))
box = num(1, 100)
while count > 0:
    if inp_box == box:
        print("Congrats! You won!")
        break
    else:
        count -= 1
        if count == 0:
            print("Game over!")
            break
        elif inp_box > box:
            inp_box = int(
                input(
                    f"Wrong number. Our number is lower. You have {count} guesses left: "
                )
            )
        elif inp_box < box:
            inp_box = int(
                input(
                    f"Wrong number. Our number is higher. You have {count} guesses left: "
                )
            )
