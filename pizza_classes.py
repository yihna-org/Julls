#   Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary


class Pizza:
    def __init__(self, size, crust_type, toppings):
        self.size = size
        self.crust_type = crust_type
        self.toppings = list(toppings)

    def new_topping(self):
        new = input("Add new topping: ")
        self.toppings.append(new)

    def rem_topping(self):
        rem = input("Remove topping: ")
        if rem in self.toppings:
            self.toppings.remove(rem)
            print("The topping has been successfully removed!")
        else:
            print("We do not have that!")

    def details(self):
        print(" ===== Your Pizza ===== ")
        print(f"Size: {self.size}\nCrust: {self.crust_type}")
        if self.toppings:
            print(f"All topings: {', '.join(self.toppings)}")
        else:
            print("No toppings yet!")


order1 = Pizza("35 cm", "thin", ["ketchup", "brbq"])
order1.new_topping()
order1.details()

order2 = Pizza("medium", "deep dish", ["chease"])
order2.rem_topping()
order2.rem_topping()
order2.details()
