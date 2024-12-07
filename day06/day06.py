#!/usr/bin/env python3

import copy
import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))



def read_input_into_table(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    map = []
    for line in lines:
        map.append([s for s in line])
    return map


class Guard:

    def __init__(self, x, y, direction, limits):
        self.x = x
        self.y = y
        self.direction = direction
        self.visited = {(x, y, direction)}
        self.limits = limits
        self.off = False

    def move(self, obstacles, additional_obstacle):
        next = self.look_forward()
        if self.is_off_limit(next[0], next[1]):
            self.off = True
            return
        if next in obstacles or next == additional_obstacle:
            self.turn()
            return
        self.x, self.y = next
        next_visited = (next[0], next[1], self.direction)
        if next_visited in self.visited:
            raise RuntimeError("Loop detected")
        self.visited.add(next_visited)

    def look_forward(self):
        match self.direction:
            case 0:
                next = (self.x, self.y - 1)
            case 1:
                next = (self.x + 1, self.y)
            case 2:
                next = (self.x, self.y + 1)
            case 3:
                next = (self.x - 1, self.y)
        return next

    def turn(self):
        self.direction = (self.direction + 1) % 4

    def is_off_limit(self, x, y):
        if x < 0 or x >= self.limits[0]:
            return True
        if y < 0 or y >= self.limits[1]:
            return True
        return False


def parse_data(map):
    obstacles = {}
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "#":
                obstacles[(x, y)] = True
            if map[y][x] == "^":
                guard_coord = (x, y)
    return Guard(
        x=guard_coord[0],
        y=guard_coord[1],
        direction=0,
        limits=(len(map[0]), len(map)),
    ), obstacles


# =========================================


def run(guard, obstacles, additional_obstacle=(-1,-1)):
    while True :
        guard.move(obstacles, additional_obstacle=additional_obstacle)
        if guard.off:
            break

def run1(guard, obstacles):
    run(guard, obstacles)
    visited = {(v[0], v[1]) for v in guard.visited}
    return len(visited), visited


# =========================================


## Without parallelization
##
# def run2(guard, obstacles, visited):
#     count = 0
#     for x, y in visited:
#         if x == guard.x and y == guard.y:
#             continue
#         if (x, y) in obstacles:
#             continue
#         test_guard = Guard(
#             x=guard.x,
#             y=guard.y,
#             direction=guard.direction,
#             limits=guard.limits,
#         )
#         try:
#             run(test_guard, obstacles, additional_obstacle=(x,y))
#         except RuntimeError:
#             count += 1
#     return count


def run_parallel(guard, obstacles, additional_obstacle):
    test_guard = Guard(
        x=guard.x,
        y=guard.y,
        direction=guard.direction,
        limits=guard.limits,
    )
    try:
        run(test_guard, obstacles, additional_obstacle)
    except RuntimeError:
        return 1
    return 0

## With parallelization
def run2(guard, obstacles, visited):
    from functools import partial
    from multiprocessing import Pool

    unary = partial(run_parallel, guard, obstacles)

    with Pool() as p:
        results = p.map(unary, visited)

    return sum(results)


# INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
board = read_input_into_table(INPUT)
guard, obstacles = parse_data(board)

start1 = time.time()
result1, visited = run1(guard, obstacles)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.3f}ms)")

guard, obstacles = parse_data(board)
start2 = time.time()
result2 = run2(guard, obstacles, visited)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.3f}ms)")
