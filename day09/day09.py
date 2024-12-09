#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> str:
    with open(path, 'r') as f:
        lines = f.read()
    return lines


def parse_data(dense_format_data):
    data = []
    file_idx = 0
    for i,d in enumerate(dense_format_data):
        if i % 2 == 0:
            data += [file_idx] * int(d)
            file_idx += 1
        if i% 2 == 1:
            data += [-1] * int(d)
    return data

# =========================================

def cheksum(data):
    checksum = 0
    for i,v in enumerate(data):
        if v != -1:
            checksum += i * v
    return checksum


def run1(data):
    i = -1
    reverse_idx = len(data) -1 
    compacted = [-1] * len(data)
    while True:
        i += 1
        compacted[i] = data[i]
        if data[i] != -1:
            continue
        while data[reverse_idx] == -1 and reverse_idx > i:
            reverse_idx -= 1
        if reverse_idx == i:
            break
        compacted[i], data[reverse_idx] = data[reverse_idx], -1
    return cheksum(compacted)



# =========================================

def run2(data):
    pass


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
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
