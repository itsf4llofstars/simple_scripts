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

if DOORS[picked_door] == "gold":  # Will always show 1st non-picked door
    for door in DOORS:
        if picked_door == door:
            continue
        print(f"Your door: {picked_door}, door {door}: {DOORS[door]}")
        break
elif DOORS[picked_door] == "goat":
    for door in DOORS:
        if picked_door == door or DOORS[door] == "gold":
            continue
        print(f"Your door: {picked_door}, door {door}: {DOORS[door]}")
elif DOORS[picked_door] == "fleas":
    for door in DOORS:
        if picked_door == door or DOORS[door] == "gold":
            continue
        print(f"Your door: {picked_door}, door {door}: {DOORS[door]}")
