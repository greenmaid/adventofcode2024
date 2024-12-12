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
        map.append([s for s in line])
    return map


# =========================================

# First implementation less performant
# def scan_regions(grid):
#     regions = {}
#     area_idx = 1
#     box_area_map = {}
#     for y, row in enumerate(grid):
#         for x, val in enumerate(row):
#             up_idx = 0
#             if y > 0 and grid[y-1][x] == val:
#                 up_idx = box_area_map[(x,y-1)]
#                 box_area_map[(x,y)] = up_idx
#             left_idx = 0
#             if x > 0 and grid[y][x-1] == val:
#                 left_idx = box_area_map[(x-1,y)]
#                 box_area_map[(x,y)] = left_idx
#             if up_idx and left_idx and up_idx != left_idx:
#                 # merge areas
#                 for k,v in box_area_map.items():
#                     if v == up_idx:
#                         box_area_map[k] = left_idx
#             if not (up_idx or left_idx):
#                 area_idx += 1
#                 box_area_map[(x,y)] = area_idx
#     for box,idx in box_area_map.items():
#         if idx not in regions:
#             regions[idx] = set()
#         regions[idx].add(box)
#     return regions


def scan_regions(grid):
    regions = {}
    area_idx = 1
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val != ".":
                area = set([(x,y)])
                discovered = set([(x,y)])
                while discovered:
                    next_discovered = set()
                    for d in discovered:
                        for nx,ny in [(d[0]+1,d[1]), (d[0]-1,d[1]), (d[0],d[1]+1), (d[0],d[1]-1)]:
                            if nx >=0 and nx < len(row) and ny >=0 and ny < len(grid):
                                if grid[ny][nx] == val:
                                    next_discovered.add((nx,ny))
                                    area.add((nx,ny))
                                    grid[ny][nx] = '.'
                    discovered = next_discovered
                regions[area_idx] = area
                area_idx += 1
    return regions


def get_perimeter(area):
    count = 0
    for x,y in area:
        if (x+1,y) not in area:
            count += 1
        if (x-1,y) not in area:
            count += 1
        if (x,y+1) not in area:
            count += 1
        if (x,y-1) not in area:
            count += 1
    return count


def get_sides(area):
    count = 0
    for x,y in area:
        if (x+1,y) not in area and (x,y-1) not in area:
            count += 1
        if (x+1,y) not in area and (x,y+1) not in area:
            count += 1
        if (x-1,y) not in area and (x,y-1) not in area:
            count += 1
        if (x-1,y) not in area and (x,y+1) not in area:
            count += 1
        if (x+1,y+1) not in area and (x+1,y) in area and (x,y+1) in area:
            count += 1
        if (x-1,y+1) not in area and (x-1,y) in area and (x,y+1) in area:
            count += 1
        if (x-1,y-1) not in area and (x-1,y) in area and (x,y-1) in area:
            count += 1
        if (x+1,y-1) not in area and (x+1,y) in area and (x,y-1) in area:
            count += 1

    return count



def run1(regions):
    price = 0
    for _,r in regions.items():
        price += len(r) * get_perimeter(r)
    return price


# =========================================

def run2(regions):
    price = 0
    for _,r in regions.items():
        price += len(r) * get_sides(r)
    return price


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
grid = read_input_into_table(INPUT)

start1 = time.time()
regions = scan_regions(grid)
result1 = run1(regions)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(regions)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
