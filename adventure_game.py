freelancers = {
    "name": "Freelancing Shop",
    "brian": 70,
    "black knight": 20,
    "biccus diccus": 100,
    "grim reaper": 500,
    "minstrel": 15,
}
antiques = {
    "name": "Antique Shop",
    "french castle": 400,
    "wooden grail": 3,
    "scythe": 150,
    "catapult": 75,
    "german joke": 5,
}
pet_shop = {"name": "Pet Shop", "blue parrot": 10, "white rabbit": 5, "newt": 2}

shops = [freelancers, antiques, pet_shop]

department_store = freelancers | antiques | pet_shop
department_store = {k: v for k, v in department_store.items() if k != "name"}
print("--------inventory before purchases--------")
print(f"Available items: {', '.join(department_store.keys())}")

purse = 1000
cart = {}

while True:
    print("Which shop do you want to visit?")
    for i, shop in enumerate(shops, start=1):
        print(f"  {i}. {shop['name']}")

    choice = input("Enter shop number (or 'exit' to leave): ").lower()

    if choice == "exit":
        break

    if not choice.isdigit() or not (1 <= int(choice) <= len(shops)):
        print("Invalid choice, try again")
        continue

    shop = shops[int(choice) - 1]
    shop_name = shop["name"]
    items = {k: v for k, v in shop.items() if k != "name"}

    buy_item = input(
        f"Welcome to {shop_name}!\nYour balance: {purse}\nWhat do you want to buy (or 'exit' to leave): {', '.join(items.keys())} - "
    ).lower()

    if buy_item == "exit":
        continue
    elif buy_item in items:
        print(f"{buy_item} added to cart")
        price = shop[buy_item]
    else:
        print("Item not found")
        continue

    cart.update({buy_item: shop.pop(buy_item)})
    purse -= price
    department_store.pop(buy_item)

print(
    f"You Purchased {', '.join(cart.keys())} - Total {sum(cart.values())}\nMoney left: {purse}\nHave a nice day of mayhem!"
)
print("--------inventory after purchases--------")
print(f"Available items: {', '.join(department_store.keys())}")
