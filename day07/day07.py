#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = f.read().splitlines()
    return lines


def parse_data(lines):
    result = []
    for line in lines:
        target, nums_str = line.split(": ")
        nums = []
        for n in nums_str.split(" "):
            nums.append(int(n))
        result.append((int(target), nums))
    return result


# =========================================


def get_combinations(nums):
    if len(nums) == 1:
        yield nums[0]
        return
    for v in get_combinations(nums[:-1]):
        yield nums[-1] + v
        yield nums[-1] * v


def run1(equations):
    count = 0
    for eq in equations:
        for n in get_combinations(eq[1]):
            if n == eq[0]:
                count += eq[0]
                break
    return count


# =========================================


def get_concatenations(nums, current=[]):
    for i, n in enumerate(mums):
        yield


def get_combinations2(nums):
    if len(nums) == 1:
        yield nums[0]
        return
    for v in get_combinations2(nums[:-1]):
        yield nums[-1] + v
        yield nums[-1] * v
        yield int(f"{v}{nums[-1]}")


def run2(equations):
    count = 0
    for eq in equations:
        for n in get_combinations2(eq[1]):
            # print(eq, eq[0], n)
            if n == eq[0]:
                count += eq[0]
                break
    return count


INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
equations = parse_data(data)

start1 = time.time()
result1 = run1(equations)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(equations)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
