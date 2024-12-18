#!/usr/bin/env python3

import os
import time
import networkx as nx
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse_data(data, count):
    coords_as_map = {}
    lines = data[:count]
    for line in lines:
         c = [int(v) for v in line.split(",")]
         coords_as_map[(c[0],c[1])] = True
    return coords_as_map


# =========================================

def run1(falling_bytes_count):
    falling_bytes = parse_data(data, falling_bytes_count)
    G = nx.Graph()
    for y in range(GRID_LIMIT):
        for x in range(GRID_LIMIT):
            if (x,y) not in falling_bytes:
                G.add_node((x,y))
                if (x-1,y) not in falling_bytes:
                    G.add_edge((x-1,y),(x,y))
                if (x,y-1) not in falling_bytes:
                    G.add_edge((x,y-1),(x,y))
    start = (0,0)
    target = (GRID_LIMIT-1,GRID_LIMIT-1)
    path = nx.shortest_path(G, source=start, target=target)
    return len(path) - 1


# =========================================

def test_path(partial_falling_bytes):
    G = nx.Graph()
    for y in range(GRID_LIMIT):
        for x in range(GRID_LIMIT):
            if (x,y) not in partial_falling_bytes:
                G.add_node((x,y))
                if (x-1,y) not in partial_falling_bytes:
                    G.add_edge((x-1,y),(x,y))
                if (x,y-1) not in partial_falling_bytes:
                    G.add_edge((x,y-1),(x,y))
    start = (0,0)
    target = (GRID_LIMIT-1,GRID_LIMIT-1)
    return nx.has_path(G, source=start, target=target)


def run2(data):
    interval = (0, len(data))
    while True:
        middle = int((interval[1] + interval[0]) / 2)
        falling_bytes = parse_data(data, middle+1)
        if test_path(falling_bytes):
            interval = (middle, interval[1])
        else:
            interval = (interval[0], middle)
        if interval[0] == interval[1]-1:
            break
    return data[interval[1]]


# INPUT = f"{SCRIPT_DIR}/input_test.txt"
# GRID_LIMIT = 7
# RUN_1_LIMIT = 12
INPUT = f"{SCRIPT_DIR}/input.txt"
GRID_LIMIT = 71
RUN_1_LIMIT = 1024

data = read_input(INPUT)

start1 = time.time()
result1 = run1(RUN_1_LIMIT)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(data)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
