#!/usr/bin/env python3
"""monty_hall.py"""
import random

doors = ["one", "two", "three"]
prizes = ["goat", "gold", "fleas"]
games = 0
max_games = 1000
win, loss = 0, 0

DOORS = {
    "1": "",
    "2": "",
    "3": "",
}

while games < max_games:
    random.shuffle(prizes)

    INDEX = 0
    for door in DOORS:
        DOORS[door] = prizes[INDEX]
        INDEX += 1

    # picked_door = input("Pick your door: ")
    picked_door = str(random.randint(1, 3))
    show_door = ""

    if DOORS[picked_door] == "gold":  # Will always show 1st non-picked door
        for door, prize in DOORS.items():
            if picked_door == door:
                continue
            show_door = door
            # print(f"Your door: {picked_door}, door {door}: {prize}")
            break
    elif DOORS[picked_door] == "goat":
        for door, prize in DOORS.items():
            if picked_door == door or prize == "gold":
                continue
            show_door = door
            # print(f"Your door: {picked_door}, door {door}: {prize}")
    elif DOORS[picked_door] == "fleas":
        for door, prize in DOORS.items():
            if picked_door == door or prize == "gold":
                continue
            show_door = door
            # print(f"Your door: {picked_door}, door {door}: {prize}")

    # switch = input("Do you want to swith? [y/n]")
    switch = "y"

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

    # print(picked_door)
    # print(DOORS[picked_door])
    if DOORS[picked_door] == "gold":
        win += 1
    else:
        loss += 1

    games += 1

print(f"{win = } {loss = }")
