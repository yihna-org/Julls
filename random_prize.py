# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names).
# 2. Use a loop to collect their names into a list.
# 3. Ask for exactly 3 prize names (in order) and store them in a list.
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats.

participants = []
prizes = ["Bronze Prize", "Silver Prize", "!Grand Prize!"]

while True:
    entering = input("Enter name for entering the raffle - ")

    if entering.lower() == "done":
        if len(participants) < 3:
            print("Need at least 3 participants")
            continue
        break

    participants.append(entering)

import random

winners = random.sample(participants, k=3)

print("------Time for Raffle Prize------")
print(f"Third place - {winners[2]}!! - {prizes[0]}!")
print(f"Second place - {winners[1]}!! - {prizes[1]}!")
print(f"First place - {winners[0]}!! - {prizes[2]}!")
