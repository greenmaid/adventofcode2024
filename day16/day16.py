#!/usr/bin/env python3

import os
import time
import networkx as nx
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input_into_table(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    map = []
    for line in lines:
        map.append([s for s in line])
    return map


def parse_data(grid):
    G = nx.Graph()
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val in "E.":
                G.add_node((x,y,"H"))
                G.add_node((x,y,"V"))
                G.add_edge((x,y,"H"), (x,y,"V"), weight=1000)
                if grid[y-1][x] in "E.":
                    G.add_edge((x,y,"V"), (x,y-1,"V"), weight=1)
                if grid[y][x-1] in "E.":
                    G.add_edge((x,y,"H"), (x-1,y,"H"), weight=1)
            if val == "S":
                G.add_node("Start")
                if grid[y][x+1] in "E.":
                    G.add_edge("Start", (x+1,y,"H"), weight=1)
                if grid[y][x-1] in "E.":
                    G.add_edge("Start", (x-1,y,"H"), weight=2001)
                if grid[y+1][x] in "E.":
                    G.add_edge("Start", (x,y+1,"V"), weight=1001)
                if grid[y-1][x] in "E.":
                    G.add_edge("Start", (x,y-1,"V"), weight=1001)
            if val == "E":
                G.add_node("End")
                G.add_edge("End", (x,y,"H"), weight=0)
                G.add_edge("End", (x,y,"V"), weight=0)
    return G

# =========================================

def display(grid, path):
    class bcolors:
        YELLOW = '\033[93m'
        ENDC = '\033[0m'
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if (x,y,"V") in path or (x,y,"H") in path:
                print(f"{bcolors.YELLOW}x{bcolors.ENDC}", end="")
            else:
                print(val, end="")
        print("")
    print("")


def run1(graph):
    # path = nx.shortest_path(graph, source="Start", target="End", weight="weight", method='dijkstra')
    # display(grid, path)
    length = nx.shortest_path_length(graph, source="Start", target="End", weight="weight", method='dijkstra')
    return length

# =========================================

def run2(graph):
    paths = nx.all_shortest_paths(graph, source="Start", target="End", weight="weight", method='dijkstra')
    seats = set((s[0], s[1]) for p in paths for s in p)
    return(len(seats)-1)


INPUT = f"{SCRIPT_DIR}/input.txt"
grid = read_input_into_table(INPUT)
graph = parse_data(grid)

start1 = time.time()
result1 = run1(graph)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(graph)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
