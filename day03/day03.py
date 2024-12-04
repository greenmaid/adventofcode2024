#!/usr/bin/env python3

import os
import re
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> str:
    with open(path, 'r') as f:
        lines = f.read()
    return lines


# =========================================

def run1(data: str):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    return sum([int(m[0]) * int(m[1]) for m in matches])

# =========================================

def run2(data: str):
    pattern = r"(?:mul\((\d+),(\d+)\)|(do\(\))|(don't\(\)))"
    matches = re.findall(pattern, data)
    enabled = True
    result = 0
    for m in matches:
        match m:
            case ('', '', 'do()', ''):
                enabled = True
            case ('', '', '', "don't()"):
                enabled = False
            case _:
                if enabled:
                    result += int(m[0]) * int(m[1])
    return result


# INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)

start1 = time.time()
result1 = run1(data)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(data)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
