#!/usr/bin/env python3

import os
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines



# =========================================

def parse_data(lines):
    result = []
    for line in lines:
        numbers = [int(val) for val in line.split(" ")]
        result.append(numbers)
    return result

def is_safe(stages):
    if stages[1] - stages[0] > 0:
        direction = "+"
    else:
        direction = "-"
    for i in range(len(stages)-1):
        diff = stages[i+1] - stages[i]
        if diff == 0 or abs(diff) > 3:
            return False
        if diff > 0 and direction == "-":
            return False
        if diff < 0 and direction == "+":
            return False
    return True


def run1(reports):
    count = 0
    for stages in reports:
        if is_safe(stages):
            count += 1
    return count

# =========================================

def is_safe2(stages):
    if is_safe(stages):
        return True
    for i in range(len(stages)):
        if is_safe(stages[:i]+stages[i+1:]):
            return True
    return False


def run2(lines: List[str]):
    count = 0
    for stages in reports:
        if is_safe2(stages):
            count += 1
    return count


INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
reports = parse_data(data)

result1 = run1(reports)
print("Result1 = ", result1)

result2 = run2(reports)
print("Result2 = ", result2)
