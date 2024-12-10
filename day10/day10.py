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


def climb(x, y, grid, current_sommets, current_count):
    height = grid[y][x]
    for next in [(0,-1), (0,1), (1,0), (-1,0)]:
        nx, ny = x + next[0], y + next[1]
        if nx >= 0 and ny >= 0 and nx < len(grid[0]) and ny < len(grid):
            next_h = grid[ny][nx]
            if next_h == height + 1:
                if height + 1 == 9:
                    current_sommets.add((nx,ny))
                    current_count += 1
                else:
                    current_sommets, current_count = climb(nx, ny, grid, current_sommets, current_count)
    return current_sommets, current_count


def run(grid):
    total_count_step1 = 0
    total_count_step2 = 0
    for b in range(len(grid)):
        for a in range(len(grid[0])):
            if grid[b][a] == 0:
                sommets, count = climb(a, b, grid, set(), 0)
                total_count_step1 += len(sommets)
                total_count_step2 += count
    return total_count_step1, total_count_step2

# =========================================

def run2(grid):
    pass


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
grid = read_input_into_table(INPUT)

start1 = time.time()
result1, result2 = run(grid)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")
print("Result2 = ", result2)
