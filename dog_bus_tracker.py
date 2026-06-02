"""
Dog Bus Tracker Module

This module manages a digital roster for a dog bus service. It initializes
a passenger dictionary mapping seat numbers to pet details, displays the
initial roster, handles dynamic seating assignment for a new pet within a
defined maximum capacity, and processes early drop-offs by removing pets
from the bus.
"""

seat_num = {
    1: {
        "name": "Lilly",
        "breed": "British",
        "pickup_time": "09:00",
        "dropoff_time": "14:00",
    },
    2: {
        "name": "Mika",
        "breed": "Scotish",
        "pickup_time": "09:00",
        "dropoff_time": "14:00",
    },
    3: {
        "name": "Alisia",
        "breed": "None",
        "pickup_time": "09:00",
        "dropoff_time": "12:00",
    },
}


# starting roster showing each pet’s seat, name, and pickup time.

print("------Starting roster list------")
for seat, pet in seat_num.items():
    name = pet.get("name", "Empty")
    pickup = pet.get("pickup_time", "—")

    print("Seat:", seat, "| Name:", name, ", Pickup at", pickup)


def available(seat_num):
    return len(seat_num)


while True:
    ava = available(seat_num)
    if ava < 8:
        name = input("Enter name of your dog - ")

        if name.lower() == "done":
            break

        breed = input("Breed of your dog - ")
        pickup_time = input("pickup_time - ")
        dropoff_time = input("dropoff_time - ")
        next = ava + 1
        seat_num[next] = {
            "name": name,
            "breed": breed,
            "pickup_time": pickup_time,
            "dropoff_time": dropoff_time,
        }
        print(f"\n👋  {name} in seat {ava+1}")
    else:
        print("Sorry! We do not have any avalable seats!")
        break

for seat, info in seat_num.items():
    name = info.get("name", "Empty")
    dropoff = info.get("dropoff_time", "—")

    print("Seat:", seat, "| Name:", name, ", Dropoff time", dropoff)


print("\n------Drop off time------")


def check_all_dropoffs(seat_num):
    to_clear = []
    for seat, info in seat_num.items():
        name = info.get("name", "Empty")
        dropoff = info.get("dropoff_time")

        if dropoff != "14:00":
            print(f"{name} is home.\nSeat {seat}: availible!")
            to_clear.append(seat)

    for seat in to_clear:
        seat_num[seat] = {}


check_all_dropoffs(seat_num)

print("\n------Final roster list------")
for seat, info in seat_num.items():
    name = info.get("name", "Empty")
    dropoff = info.get("dropoff_time", "—")
    print("Seat:", seat, "| Name:", name, ", Dropoff time", dropoff)
