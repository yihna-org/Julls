import random

user_answ = None
cups = ["empty", "empty", "BALL!"]
while True:
    while user_answ not in [1, 2, 3]:
        user_answ = int(input("Chouse cup(1,2,3) - "))
    random.shuffle(cups)
    cup = cups[user_answ - 1]
    print(cup)
    if cup == "empty":
        print("Next time!")
    else:
        print("Congrats! You won!")
    break
