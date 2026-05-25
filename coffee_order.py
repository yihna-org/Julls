# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price

total = 0
drink_count = 0

while True:
    name = input("Enter your name - ")
    if name == "done":
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
