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
    raw_towels, raw_patterns = data.split("\n\n")
    towels = raw_towels.split(", ")
    patterns = raw_patterns.split("\n")
    return towels, patterns

# =========================================

CACHE = {}

def is_design_possible(pattern, towels, current=0):
    if pattern in CACHE:
        return current + CACHE[pattern]
    new = current
    for t in towels:
        if t == pattern:
            new += 1
        elif pattern.startswith(t):
            new = is_design_possible(pattern[len(t):], towels, new)
    CACHE[pattern] = new - current
    return new


def run(towels, patterns):
    count1 = 0
    count2 = 0
    for p in patterns:
        res = is_design_possible(p, towels)
        if res > 0:
            count1 += 1
            count2 += res
    return count1, count2


INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
towels, patterns = parse_data(data)

start1 = time.time()
result1, result2 = run(towels, patterns)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")
print("Result2 = ", result2)
