#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> str:
    with open(path, "r") as f:
        lines = f.read()
    return lines


def parse_data(dense_format_data):
    data = []
    file_idx = 0
    for i, d in enumerate(dense_format_data):
        if i % 2 == 0:
            data += [file_idx] * int(d)
            file_idx += 1
        if i % 2 == 1:
            data += [-1] * int(d)
    return data


# =========================================


def cheksum(data):
    checksum = 0
    for i, v in enumerate(data):
        if v != -1:
            checksum += i * v
    return checksum


def run1(data):
    i = -1
    reverse_idx = len(data) - 1
    compacted = [-1] * len(data)
    while True:
        i += 1
        if data[i] != -1:
            compacted[i] = data[i]
            continue
        while data[reverse_idx] == -1 and reverse_idx > i:
            reverse_idx -= 1
        if reverse_idx == i:
            break
        compacted[i], data[reverse_idx] = data[reverse_idx], -1
    return cheksum(compacted)


# =========================================


def run2(data):
    idx = len(data) - 1
    target_id = max(data)
    compacted = data
    while target_id >= 0:
        buff = 0
        while idx >= 0 and (compacted[idx] == -1 or compacted[idx] >= target_id):
            if compacted[idx] == target_id:
                buff += 1
                start = idx
            idx -= 1
        target_slice = compacted[start : start + buff]
        target_id -= 1

        buff = 0
        empty_end = -2
        for i in range(start):
            if compacted[i] != -1:
                buff = 0
                continue
            buff += 1
            if buff == len(target_slice):
                empty_end = i
                break
        if empty_end != -2:
            compacted[empty_end - len(target_slice) + 1 : empty_end + 1] = target_slice
            compacted[start : start + len(target_slice)] = [-1] * len(target_slice)
    return cheksum(compacted)


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
parsed = parse_data(data)

start1 = time.time()
result1 = run1(parsed)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

parsed = parse_data(data)
start2 = time.time()
result2 = run2(parsed)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
