#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_inputinto_table(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    map = []
    for line in lines:
        map.append([s for s in line])
    return map


def parse_data(lines):
    return lines

# =========================================

def find_XMAS_at_position(x, y, table):
    if table[y][x] != "X":
        return 0
    count = 0
    dimX = len(table[0])
    dimY = len(table)
    if x < dimX - 3:
        if table[y][x+1] == "M" and table[y][x+2] == "A" and table[y][x+3] == "S":
            count += 1

    if x > 2:
        if table[y][x-1] == "M" and table[y][x-2] == "A" and table[y][x-3] == "S":
            count += 1

    if y < dimY - 3:
        if table[y+1][x] == "M" and table[y+2][x] == "A" and table[y+3][x] == "S":
            count += 1

    if y > 2:
        if table[y-1][x] == "M" and table[y-2][x] == "A" and table[y-3][x] == "S":
            count += 1

    if x < dimX - 3 and y < dimY - 3:
        if table[y+1][x+1] == "M" and table[y+2][x+2] == "A" and table[y+3][x+3] == "S":
            count += 1

    if x < dimX - 3 and y > 2:
        if table[y-1][x+1] == "M" and table[y-2][x+2] == "A" and table[y-3][x+3] == "S":
            count += 1

    if x > 2 and y > 2:
        if table[y-1][x-1] == "M" and table[y-2][x-2] == "A" and table[y-3][x-3] == "S":
            count += 1

    if x > 2 and y < dimY - 3:
        if table[y+1][x-1] == "M" and table[y+2][x-2] == "A" and table[y+3][x-3] == "S":
            count += 1

    return count


def run1(table: List[List[str]]):
    count = 0
    for y,row in enumerate(table):
        for x,_ in enumerate(row):
            count += find_XMAS_at_position(x,y,table)
    return count

# =========================================

def find_X_MAS_at_position(x, y, table):
    if table[y][x] != "A":
        return 0
    dimX = len(table[0])
    dimY = len(table)
    if x > 0 and x < dimX - 1 and y > 0 and y < dimY - 1:
        elems = [table[y+1][x-1], table[y-1][x-1], table[y+1][x+1], table[y-1][x+1]]
        if sorted(elems) ==  ["M", "M", "S", "S"]:
            if elems[0] == elems[3]:
                return 0
            else:
                return 1
    return 0

def run2(table: List[List[str]]):
    count = 0
    for y,row in enumerate(table):
        for x,_ in enumerate(row):
            count += find_X_MAS_at_position(x,y,table)
    return count


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
table = read_inputinto_table(INPUT)

start1 = time.time()
result1 = run1(table)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(table)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
