#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input_into_table(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    map = []
    for line in lines:
        map.append([int(s) for s in line])
    return map


# =========================================


def climb(x, y, grid, current_sommets):
    height = grid[y][x]
    for next in [(0,-1), (0,1), (1,0), (-1,0)]:
        nx, ny = x + next[0], y + next[1]
        if nx >= 0 and ny >= 0 and nx < len(grid[0]) and ny < len(grid):
            next_h = grid[ny][nx]
            if next_h == height + 1:
                if height + 1 == 9:
                    current_sommets.add((nx,ny))
                else:
                    current_sommets = climb(nx, ny, grid, current_sommets)
    return current_sommets


def run1(grid):
    total_count = 0
    for b in range(len(grid)):
        for a in range(len(grid[0])):
            if grid[b][a] == 0:
                sommets = climb(a, b, grid, set())
                total_count += len(sommets)
    return total_count

# =========================================

def run2(grid):
    pass


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
grid = read_input_into_table(INPUT)

start1 = time.time()
result1 = run1(grid)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(grid)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
