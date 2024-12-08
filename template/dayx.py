#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def read_input_into_table(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    map = []
    for line in lines:
        map.append([s for s in line])
    return map


def parse_data(lines):
    return lines

# =========================================

def run1(lines: List[str]):
    pass

# =========================================

def run2(lines: List[str]):
    pass


INPUT = f"{SCRIPT_DIR}/input_test.txt"
# INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
parsed = parse_data(data)

start1 = time.time()
result1 = run1(parsed)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(parsed)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
