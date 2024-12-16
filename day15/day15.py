#!/usr/bin/env python3

import os
import time
from typing import List


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        data = f.read().split("\n\n")
    return data


def parse_data(data):
    grid = data[0].split("\n")
    for i, row in enumerate(grid):
        grid[i] = list(row)
    moves = data[1].replace("\n", "")
    return grid, moves

# =========================================

def grid_at(pos, grid):
    return grid[pos[1]][pos[0]]


def set_grid_at(pos, val, grid):
    grid[pos[1]][pos[0]] = val


def get_position(grid):
    position = None
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "@":
                position = (x,y)
                break
        if position:
            break
    return position


def next(pos, direction, grid):
    match direction:
        case "^":
            d = (0,-1)
        case "v":
            d = (0,1)
        case ">":
            d = (1,0)
        case "<":
            d = (-1,0)
    next_pos = (pos[0]+d[0], pos[1]+d[1])
    return next_pos, grid_at(next_pos, grid)


def scan_forward(pos, direction, grid):
    scan_pos = pos
    while True:
        scan_pos, scan_val = next(scan_pos, direction, grid)

        if scan_val == "#":
            return None
        if scan_val == '.':
            return scan_pos


def can_be_moved(l,r, direction, grid, current=[]):
    match direction:
        case "^":
            d = (0,-1)
        case "v":
            d = (0,1)
    next_l = (l[0]+d[0], l[1]+d[1])
    next_r = (r[0]+d[0], r[1]+d[1])
    if grid_at(next_l, grid) == "." and grid_at(next_r, grid) == ".":
        return current + [l,r]
    if grid_at(next_l, grid) == "#" or grid_at(next_r, grid) == "#":
        return False
    if grid_at(next_l, grid) == "[":
        if grid_at(next_r, grid) != "]":
            display(grid)
            raise RuntimeError("broken crate !!")
        return can_be_moved(next_l,next_r, direction, grid, current + [l,r])

    to_move_l = []
    if grid_at(next_l, grid) == "]":
        to_move_l = can_be_moved((next_l[0]-1, next_l[1]),next_l, direction, grid, [])
        if not to_move_l:
            return False
    to_move_r = []
    if grid_at(next_r, grid) == "[":
        to_move_r = can_be_moved(next_r, (next_r[0]+1, next_r[1]), direction, grid, [])
        if not to_move_r:
            return False
    
    to_move = list(set(current + [l, r] + to_move_l + to_move_r))
    to_move.sort(key=lambda x: x[1])
    if direction == "^":
        to_move.reverse()
    return to_move


def move(position, direction, grid):
    next_pos, next_val = next(position, direction, grid)
    if next_val == "#":
        return position
    if next_val == ".":
        set_grid_at(next_pos, "@", grid)
        set_grid_at(position, ".", grid)
        return next_pos
    if next_val == "O":
        next_empty = scan_forward(next_pos, direction, grid)
        if next_empty:
            set_grid_at(next_empty, "O", grid)
            set_grid_at(next_pos, "@", grid)
            set_grid_at(position, ".", grid)
            return next_pos
        else:
            return position
    if next_val in ["[", "]"]:
        if direction in ["<", ">"]:
            next_empty = scan_forward(next_pos, direction, grid)
            if next_empty:
                row = grid[position[1]]
                if direction == ">":
                    grid[position[1]] = row[:position[0]] + ["."] + row[position[0]:next_empty[0]] + row[next_empty[0]+1:]
                if direction == "<":
                    grid[position[1]] = row[:next_empty[0]] + row[next_empty[0]+1:position[0]+1] + ["."]  + row[position[0]+1:]
                return next_pos
            else:
                return position
        if direction in ["^", "v"]:
            crates_to_move = []
            if next_val == "[":
                crates_to_move = can_be_moved(next_pos, (next_pos[0]+1, next_pos[1]), direction, grid)
            if next_val == "]":
                crates_to_move = can_be_moved((next_pos[0]-1, next_pos[1]), next_pos, direction, grid)
            if not crates_to_move:
                return position
            while crates_to_move != []:
                c = crates_to_move.pop()
                val = grid_at(c, grid)
                n, _ = next(c, direction, grid)
                set_grid_at(n, val, grid)
                set_grid_at(c, '.', grid)
            set_grid_at(next_pos, "@", grid)
            set_grid_at(position, ".", grid)
            return next_pos


def display(grid):
    class bcolors:
        YELLOW = '\033[93m'
        ENDC = '\033[0m'

    for row in grid:
        for c in row:
            if c =="@":
                print(f"{bcolors.YELLOW}@{bcolors.ENDC}", end="")
            else:
                print(c, end="")
        print("")
    print("")


def count_GPS_sum(grid):
    sum = 0
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "O" or val == "[":
                sum += x + (100*y)
    return sum


def check(position, grid):
    # check position
    if grid_at(position, grid) != "@":
        display(grid)
        raise RuntimeError(f"Something goes wrong: position {position}")
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "[":
                if grid[y][x+1] != "]":
                    display(grid)
                    raise RuntimeError(f"broken crate !! {(x,y)}")
            if val == "]":
                if grid[y][x-1] != "[":
                    display(grid)
                    raise RuntimeError(f"broken crate !! {(x,y)}")


def run1(grid, moves):
    position = get_position(grid)
    for dir in moves:
        position = move(position, dir, grid)
    return count_GPS_sum(grid)


# =========================================

def mutate_to_large_grid(grid):
    for y, row in enumerate(grid):
        new_row = []
        for val in row:
            if val == "#":
                new_row.append("#")
                new_row.append("#")
            if val == "O":
                new_row.append("[")
                new_row.append("]")
            if val == ".":
                new_row.append(".")
                new_row.append(".")
            if val == "@":
                new_row.append("@")
                new_row.append(".")
        grid[y] = new_row


def run2(grid, moves):
    mutate_to_large_grid(grid)
    position = get_position(grid)
    for dir in moves:
        position = move(position, dir, grid)
        # check(position, grid)
    return count_GPS_sum(grid)


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)

grid, moves = parse_data(data)
start1 = time.time()
result1 = run1(grid, moves)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

grid, moves = parse_data(data)
start2 = time.time()
result2 = run2(grid, moves)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
