import random

game = ["Rock", "Paper", "Scissors"]
print("Welcome to game 'rock, paper, scissors!'\n*for exit print 'done'*")

while True:
    computer_choice = random.choice(game)
    user_choice = input("Rock, paper, scissors? ").capitalize()
    if user_choice == "Done":
        print("Game over!")
        break
    if user_choice not in game:
        print("Invalid choice!")
        continue
    print(f"Computer chose: {computer_choice}")
    if computer_choice == user_choice:
        print("We have a tie!")
    elif (
        (computer_choice == "Paper" and user_choice == "Rock")
        or (computer_choice == "Rock" and user_choice == "Scissors")
        or (computer_choice == "Scissors" and user_choice == "Paper")
    ):
        print("The computer won!")
    else:
        print("You won!")
