#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse(lines):
    list1 = []
    list2 = []
    for line in lines:
        match line.split(" "):
            case [val1, '', '', val2]:
                list1.append(int(val1))
                list2.append(int(val2))
    return sorted(list1), sorted(list2)


def run1(list1, list2):
    count = 0
    for i in range(len(list1)):
        count += abs(list1[i] - list2[i])
    return count
    pass

# =========================================

def run2(list1, list2):
    similarity = 0
    for i in list1:
        similarity += i * list2.count(i)
    return similarity


# =========================================

INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
lines = read_input(INPUT)
list1, list2 = parse(lines)

start1 = time.time()
result1 = run1(list1, list2)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(list1, list2)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
