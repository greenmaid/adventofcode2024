#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read()
    return lines


def parse_data(data):
    stones = []
    for s in data.split(" "):
        stones.append(int(s))
    return stones

# =========================================

CACHE = {0: [1]}

def next(s):
    if s in CACHE:
        return CACHE[s]
    digits_count = len(str(s))
    if digits_count % 2 == 0:
        middle = int(digits_count/2)
        result = [int(str(s)[:middle]), int(str(s)[middle:])]
    else:
        result = [s * 2024]
    CACHE[s] = result
    return result

## First naive try, run well for star 1
# def run(stones, iterations):
#     for i in range(iterations):
#         new =[]
#         for s in stones:
#             new += next(s)
#         stones = new
#     return len(stones)

# =========================================

COUNT_CACHE = {}

def count_generated_stones(s,i):
    if (s,i) in COUNT_CACHE:
        return COUNT_CACHE[(s,i)]
    n = next(s)
    if i == 1:
        result = len(n)
    elif len(n) == 1:
        result = count_generated_stones(n[0],i-1)
    elif len(n) == 2:
        result = count_generated_stones(n[0],i-1) + count_generated_stones(n[1],i-1)
    COUNT_CACHE[(s,i)] = result
    return result


def run(stones, iterations):
    result = 0
    for s in stones:
        result += count_generated_stones(s, iterations)
    return result


INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
stones = parse_data(data)

start1 = time.time()
result1 = run(stones, 25)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run(stones, 75)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
