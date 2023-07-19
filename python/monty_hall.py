#!/usr/bin/env python3
"""monty_hall.py"""
import random

doors = ["one", "two", "three"]
prizes = ["goat", "gold", "fleas"]

DOORS = {
    "1": "",
    "2": "",
    "3": "",
}

random.shuffle(prizes)

INDEX = 0
for door in DOORS:
    DOORS[door] = prizes[INDEX]
    INDEX += 1

picked_door = input("Pick your door: ")
# picked_door = "2"
show_door = ""

if DOORS[picked_door] == "gold":  # Will always show 1st non-picked door
    for door, prize in DOORS.items():
        if picked_door == door:
            continue
        show_door = door
        print(f"Your door: {picked_door}, door {door}: {DOORS[door]}")
        break
elif DOORS[picked_door] == "goat":
    for door, prize in DOORS.items():
        if picked_door == door or prize == "gold":
            continue
        show_door = door
        print(f"Your door: {picked_door}, door {door}: {DOORS[door]}")
elif DOORS[picked_door] == "fleas":
    for door, prize in DOORS.items():
        if picked_door == door or prize == "gold":
            continue
        show_door = door
        print(f"Your door: {picked_door}, door {door}: {DOORS[door]}")

switch = input("Do you want to swith? [y/n]")
if switch == "y":
    if picked_door == "1":
        if show_door == "2":
            picked_door = "3"
        elif show_door == "3":
            picked_doo = "2"
    elif picked_door == "2":
        if show_door == "1":
            picked_door = "3"
        elif show_door == "3":
            picked_door = "1"
    elif picked_door == "3":
        if show_door == "1":
            picked_door = "2"
        elif show_door == "2":
            picked_door = "1"

print(picked_door)
print(DOORS[picked_door])
