#!/usr/bin/env python3
import random
import sys

doors = ["one", "two", "three"]
prizes = ["goat", "gold", "goat"]

door_dict = {
    "1": "",
    "2": "",
    "3": "",
}

win, lose = 0, 0

for _ in range(len(prizes) ** len(prizes)):
    random.shuffle(prizes)

index = 0
for k in door_dict.keys():
    door_dict[k] = prizes[index]
    index += 1
del index

for k, v in door_dict.items():
    print(k, v)
print()

# for testing
# door_choice = input("Enter your door choice 1, 2, 3: ")
door_choice = "2"

show_door = ""
for door in door_dict.keys():
    if door == door_choice or door_dict[door] == "gold":
        continue
    show_door = door
    print(f"Door: {show_door} is a {door_dict[door]}")

swap: bool = None

# for testing
# switch = input("Do you want to switch [y/n]? ")
switch = "y"

if switch == "y":
    swap = True
else:
    swap = False

if swap:
    for door in door_dict.keys():
        if door_dict[door] == "gold":
            win += 1
        else:
            lose += 1
else:
    if door_dict[door_choice] == "gold":
        win += 1
    else:
        lose += 1

print()
print(door_choice)
for k, v in door_dict.items():
    print(k, v)
print(f"{win = } {lose = }")
