#!/usr/bin/env python3

import os
import time
import networkx
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
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "S":
                start = (x,y)
                grid[y][x] = "."
            if val == "E":
                end = (x,y)
                grid[y][x] = "."
    return start, end

# =========================================


def get_circuit(start, end, grid):
    G = networkx.Graph()
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "#":
                continue
            G.add_node((x,y))
            if grid[y][x-1] == ".":
                G.add_edge((x,y),(x-1,y))
            if grid[y-1][x] == ".":
                G.add_edge((x,y),(x,y-1))
    circuit = networkx.shortest_path(G, start, end)
    circuit_points = {x:i for i,x in enumerate(circuit)}
    return circuit, circuit_points

def run1(circuit, circuit_points, grid):
    shortcuts = {}
    def sc():
        if (nx,ny) in circuit_points and circuit_points[(nx,ny)] > circuit_points[(x,y)]:
            shortcuts[((x,y),(nx,ny))] = circuit_points[(nx,ny)] - circuit_points[(x,y)] - 2

    for x, y in circuit:
        if x > 0 and grid[y][x-1] == "#":
            ox, oy = x - 1, y
            nx, ny = x - 2, y
            sc()
            nx, ny = x - 1, y - 1
            sc()
            nx, ny = x - 1, y + 1
            sc()
        if x < len(grid[0]) - 1 and grid[y][x+1] == "#":
            ox, oy = x + 1, y
            nx, ny = x + 2, y
            sc()
            nx, ny = x + 1, y - 1
            sc()
            nx, ny = x + 1, y + 1
            sc()
        if y > 0 and grid[y-1][x] == "#":
            ox, oy = x, y - 1
            nx, ny = x, y - 2
            sc()
            nx, ny = x - 1, y - 1
            sc()
            nx, ny = x + 1, y - 1
            sc()
        if y < len(grid) - 1 and grid[y+1][x] == "#":
            ox, oy = x, y + 1
            nx, ny = x, y + 2
            sc()
            nx, ny = x + 1, y + 1
            sc()
            nx, ny = x - 1, y + 1
            sc()

    return len([k for k,v in shortcuts.items() if v >= 100])

# =========================================

def run2(circuit, circuit_points, grid):
    shortcuts = {}
    for i, p  in enumerate(circuit):
        x, y = p
        for nx, ny in circuit[i+100:]:
            if abs(nx-x) + abs(ny-y) <= 20:
                shortcuts[((x,y),(nx,ny))] = circuit_points[(nx,ny)] - circuit_points[(x,y)] - abs(nx-x) - abs(ny-y)

    return len([k for k,v in shortcuts.items() if v >= 100])


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
grid = read_input_into_table(INPUT)
start, end = parse_data(grid)

start1 = time.time()
circuit, circuit_points = get_circuit(start, end, grid)
result1 = run1(circuit, circuit_points, grid)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(circuit, circuit_points, grid)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
