import random

user_answ = None
cups = ["empty", "empty", "BALL!"]
valid_answ = [1, 2, 3]
while True:
    while user_answ not in valid_answ:
        user_answ = int(input("Chouse cup(1,2,3) - "))
    random.shuffle(cups)
    cup = cups[user_answ - 1]
    print(cup)
    if cup == "empty":
        print("Next time!")
    else:
        print("Congrats! You won!")
    break
