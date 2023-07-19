#!/usr/bin/env python3
import random

bools = [False, True]

doors =[1, 2, 3]
game_doors = ['goat', 'gold', 'goat']

win = 0
lose = 0
games = 0
max_games = 1_000

print()
print("Switch = random")
while True:
    games += 1
    random.shuffle(game_doors)

    player_door = random.choice(doors) - 1
    switch = random.choice(bools)
    prize = game_doors[player_door]

    # [print(door, end=" ") for door in game_doors]
    # print()
    # print(player_door)
    # print(switch)
    # print(prize)

    if prize == 'gold':
        if switch:
            lose += 1
        else:
            win += 1
    elif prize == 'goat':
        if switch:
            win += 1
        else:
            lose += 1

    if games == max_games:
        break

win_pct = round(win / games * 100, 1)
lose_pct = round(lose / games * 100, 1)
print(f"{win = }, {lose = }")
print(f"{win_pct = }%, {lose_pct = }%")


win = 0
lose = 0
games = 0
switch = True
print()
print("Switch = True")
while True:
    games += 1
    random.shuffle(game_doors)

    player_door = random.choice(doors) - 1
    prize = game_doors[player_door]

    # [print(door, end=" ") for door in game_doors]
    # print()
    # print(player_door)
    # print(switch)
    # print(prize)

    if prize == 'gold':
        if switch:
            lose += 1
        else:
            win += 1
    elif prize == 'goat':
        if switch:
            win += 1
        else:
            lose += 1

    if games == max_games:
        break

win_pct = round(win / games * 100, 1)
lose_pct = round(lose / games * 100, 1)
print(f"{win = }, {lose = }")
print(f"{win_pct = }%, {lose_pct = }%")

win = 0
lose = 0
games = 0
switch = False
print()
print("Switch = False")
while True:
    games += 1
    random.shuffle(game_doors)

    player_door = random.choice(doors) - 1
    prize = game_doors[player_door]

    # [print(door, end=" ") for door in game_doors]
    # print()
    # print(player_door)
    # print(switch)
    # print(prize)

    if prize == 'gold':
        if switch:
            lose += 1
        else:
            win += 1
    elif prize == 'goat':
        if switch:
            win += 1
        else:
            lose += 1

    if games == max_games:
        break

win_pct = round(win / games * 100, 1)
lose_pct = round(lose / games * 100, 1)
print(f"{win = }, {lose = }")
print(f"{win_pct = }%, {lose_pct = }%")