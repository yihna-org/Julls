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


def roster_list():
    """
    Displays a list of seats in the vehicle.

    For each seat in the `seat_num`, it prints:
    - the seat number
    - the passenger's name (or 'Empty' if the seat is empty)
    - the boarding time (or '—' if not specified)
    """
    for seat, pet in seat_num.items():
        name = pet.get("name", "Empty")
        pickup = pet.get("pickup_time", "—")
        print(f"Seat: {seat} | Name: {name} | Pickup at {pickup}")


def available(seat_num):
    """
    Returns the number of occupied seats.

    Args:
        seat_num (dict): A dictionary where the key is the seat number.

    Returns:
        int: The number of keys in the dictionary.
    """

    return len(seat_num)


while True:
    available_seats = available(seat_num)
    if available_seats < 8:
        name = input("Enter name of your dog (or 'done' for exit) - ")

        if name.lower() == "done":
            break

        breed = input("Breed of your dog - ")
        pickup_time = input("pickup_time - ")
        dropoff_time = input("dropoff_time - ")
        next = available_seats + 1
        seat_num[next] = {
            "name": name,
            "breed": breed,
            "pickup_time": pickup_time,
            "dropoff_time": dropoff_time,
        }
        print(f"\n👋  {name} in seat {available_seats+1}")
    else:
        print("Sorry! We do not have any avalable seats!")
        break

print(roster_list())

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
print(roster_list())
