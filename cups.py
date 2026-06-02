import random

user_answ = None
cups = ["empty", "empty", "BALL!"]
valid_answ = [1, 2, 3]
while True:
    user_answ = input("Chouse cup(1,2,3) or print 'exit' - ")
    if user_answ.lower() == "exit":
        break
    user_answ = int(user_answ)
    if user_answ not in valid_answ:
        print("Invalid input. Please try again.")
        continue
    random.shuffle(cups)
    cup = cups[user_answ - 1]
    print(cup)
    if cup == "empty":
        print("Next time!")
    else:
        print("Congrats! You won!")
    break
