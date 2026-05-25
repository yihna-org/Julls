# create stores
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

# Ver 1.5 print inventory before and after purchases
department_store = freelancers | antiques | pet_shop
department_store = {k: v for k, v in department_store.items() if k != "name"}
print("--------inventory before purchases--------")
print(f"Available items: {', '.join(department_store.keys())}")

# ver 1.3 Add purse with 1000 gold pieces
purse = 1000

# create an dempty shopping cart
cart = {}

# loop through stores/dicts
for shop in (freelancers, antiques, pet_shop):
    shop_name = shop["name"]
    items = {k: v for k, v in shop.items() if k != "name"}

    buy_item = input(
        f"Welcome to {shop_name}!\nYour balance: {purse} what do you want to buy: {', '.join(items.keys())} - "
    ).lower()
    # ver 1.2 add ability to exit a store
    if buy_item == "exit" or buy_item not in items:
        continue
    elif buy_item in items:
        print(f"{buy_item} added to cart")
        price = shop[buy_item]
    else:
        print("Item not found")
    cart.update({buy_item: shop.pop(buy_item)})
    purse -= price
    department_store.pop(buy_item)
print(
    f"You Purchased {', '.join(cart.keys())} -Total {sum(cart.values())}\nMoney left: {purse}\nHave a nice day of mayhem!"
)


print("--------inventory after purchases--------")
print(f"Available items: {', '.join(department_store.keys())}")
