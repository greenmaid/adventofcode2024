#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return [ int(l) for l in lines]

# =========================================

def generate(secret):
    step1 = (secret ^ (secret * 64)) % 16777216
    step2 = (step1 ^ int(step1 / 32)) % 16777216
    step3 = (step2 ^ (step2 * 2048)) % 16777216
    return step3


def run1(data):
    announces = {}
    result = 0
    for n in data:
        CHECK_UNIQ = {}
        s = n
        pr = s % 10
        prices = [pr]
        for i in range(1, 2001):
            s = generate(s)
            pr = s % 10
            prices.append(pr)
            if i > 3:
                seq = (prices[i-3]-prices[i-4], prices[i-2]-prices[i-3], prices[i-1]-prices[i-2], prices[i]-prices[i-1])
                if seq in CHECK_UNIQ:
                    continue
                if seq not in announces:
                    announces[seq] = 0
                announces[seq] += pr
                CHECK_UNIQ[seq] = True
        result += s
    return result, announces


# =========================================

def run2(announces):
    return max(announces.values())


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)

start1 = time.time()
result1, announces  = run1(data)
duration1= (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(announces)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
