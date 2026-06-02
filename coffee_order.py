"""
Coffee Order Queue Module

This module manages a simple coffee ordering queue via the command line.
It tracks the total price and the number of drinks ordered until the user
types "done" as the customer name. Supported drinks include latte, americano,
and espresso.
"""

total = 0
drink_count = 0

while True:
    name = input("Enter your name (or type 'done' for exit) - ")
    if name.lower() == "done":
        break

    order = input("What do you want to drink? ")

    if order.lower() == "latte":
        total += 3.50
    elif order.lower() == "americano":
        total += 3.00
    elif order.lower() == "espresso":
        total += 2.50
    else:
        print("Sorry, we don`t have that. Pleace order somethink different")
        continue
    drink_count += 1
print(f"You`ve ordered {drink_count}, you need to pay {total}")
