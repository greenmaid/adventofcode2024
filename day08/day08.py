#!/usr/bin/env python3

import itertools
from operator import truediv
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


def parse_data(board):
    antennas = {}
    for y in range(len(board)):
        for x in range(len(board[0])):
            val = board[y][x]
            if val == '.':
                continue
            if val not in antennas:
                antennas[val] = []
            antennas[val].append((x,y))
    return antennas

# =========================================

def run1(board, antennas):
    lim_x = len(board[0])
    lim_y = len(board)
    antinodes = set()
    for _,locations in antennas.items():
        if len(locations) > 1:
            couples = itertools.combinations(locations, 2)
            for a1, a2 in couples:
                antinode1 = (2 * a1[0] - a2[0], 2 * a1[1] - a2[1])
                if antinode1[0] >= 0 and antinode1[0] < lim_x and  antinode1[1] >= 0 and antinode1[1] < lim_y:
                    antinodes.add(antinode1)
                antinode2 = (2 * a2[0] - a1[0], 2 * a2[1] - a1[1])
                if antinode2[0] >= 0 and antinode2[0] < lim_x and  antinode2[1] >= 0 and antinode2[1] < lim_y:
                    antinodes.add(antinode2)
    return len(antinodes)

# =========================================

def run2(board, antennas):
    lim_x = len(board[0])
    lim_y = len(board)
    antinodes = set()
    for _,locations in antennas.items():
        if len(locations) > 1:
            couples = itertools.combinations(locations, 2)
            for a1, a2 in couples:

                antinodes.add(a1)
                antinodes.add(a2)

                n = 0
                while True:
                    n += 1
                    antinode1 = (a1[0] - (n * (a2[0] - a1[0])) , a1[1] - (n * (a2[1] - a1[1])))
                    if antinode1[0] >= 0 and antinode1[0] < lim_x and  antinode1[1] >= 0 and antinode1[1] < lim_y:
                        antinodes.add(antinode1)
                    else:
                        break

                n = 0
                while True:
                    n += 1
                    antinode2 = (a2[0] - (n * (a1[0] - a2[0])) , a2[1] - (n * (a1[1] - a2[1])))
                    if antinode2[0] >= 0 and antinode2[0] < lim_x and  antinode2[1] >= 0 and antinode2[1] < lim_y:
                        antinodes.add(antinode2)
                    else:
                        break
    return len(antinodes)


INPUT = f"{SCRIPT_DIR}/input.txt"
board = read_input_into_table(INPUT)
antennas = parse_data(board)

start1 = time.time()
result1 = run1(board, antennas)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(board, antennas)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
