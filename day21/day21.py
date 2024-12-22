#!/usr/bin/env python3

import os
import time
from tracemalloc import start
import networkx as nx # type: ignore
from typing import List
from itertools import product

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


NUMPAD = nx.DiGraph(
    [
        ('A', '0', {'direction': "<"}),
        ('A', '3', {'direction': "^"}),

        ('0', 'A', {'direction': ">"}),
        ('0', '2', {'direction': "^"}),

        ('3', 'A', {'direction': "v"}),
        ('3', '2', {'direction': "<"}),
        ('3', '6', {'direction': "^"}),

        ('2', '0', {'direction': "v"}),
        ('2', '1', {'direction': "<"}),
        ('2', '5', {'direction': "^"}),
        ('2', '3', {'direction': ">"}),

        ('1', '4', {'direction': "^"}),
        ('1', '2', {'direction': ">"}),

        ('4', '1', {'direction': "v"}),
        ('4', '7', {'direction': "^"}),
        ('4', '5', {'direction': ">"}),

        ('5', '2', {'direction': "v"}),
        ('5', '4', {'direction': "<"}),
        ('5', '8', {'direction': "^"}),
        ('5', '6', {'direction': ">"}),

        ('6', '3', {'direction': "v"}),
        ('6', '5', {'direction': "<"}),
        ('6', '9', {'direction': "^"}),

        ('7', '4', {'direction': "v"}),
        ('7', '8', {'direction': ">"}),

        ('8', '5', {'direction': "v"}),
        ('8', '7', {'direction': "<"}),
        ('8', '9', {'direction': ">"}),

        ('9', '6', {'direction': "v"}),
        ('9', '8', {'direction': "<"}),
    ]
)

ARROW_PAD = nx.DiGraph(
    [
        ('A', '^', {'direction': "<"}),
        ('A', '>', {'direction': "v"}),

        ('^', 'v', {'direction': "v"}),
        ('^', 'A', {'direction': ">"}),

        ('>', 'v', {'direction': "<"}),
        ('>', 'A', {'direction': "^"}),

        ('v', '<', {'direction': "<"}),
        ('v', '^', {'direction': "^"}),
        ('v', '>', {'direction': ">"}),

        ('<', 'v', {'direction': ">"}),

    ]
)

def choose_best(s):
    if len(s) == 1:
        return s[0]
    best_seqs = []
    max = -1
    for seq in s:
        count = 0
        for i in range(len(seq)-1):
            if seq[i] == seq[i+1]:
                count += 1
        if count > max:
            max = count
            best_seq = [seq]
        if count == max:
            best_seq.append(seq)

    if len(best_seq) == 1:
        return best_seq[0]

    if "<" in s[0]:
        # keep only seq starting with "<"
        best_seqs = [x for x in best_seqs if x[0].startswith("<")]
    elif "v" in s[0]:
        # keep only seq starting with "v"
        best_seqs = [x for x in best_seqs if x[0].startswith("v")]
    # take seq contains most double direction
    return best_seq[0]


CACHE = {}
def translate_dir(start, d):
    if (start, d) in CACHE:
        return CACHE[(start, d)]
    paths = nx.all_shortest_paths(ARROW_PAD, start, d)
    s = [ "".join([ARROW_PAD[u][v]['direction'] for u, v in zip(path[:-1], path[1:])]) for path in paths]
    seq = choose_best(s) + "A"
    CACHE[(start, d)] = seq
    return seq


CACHE_SEQ = {}
def translate_seq(sequence, n):
    if n == 0:
        return len(sequence)
    if (sequence, n) in CACHE_SEQ:
        return CACHE_SEQ[(sequence, n)]
    start = "A"
    count = 0
    for d in sequence:
        seq = translate_dir(start, d)
        count += translate_seq(seq, n-1)
        start = d
    CACHE_SEQ[(sequence, n)] = count
    return count


def tanslate_digit(start, digit, n):
    paths = nx.all_shortest_paths(NUMPAD, start, digit)
    s = [ "".join([NUMPAD[u][v]['direction'] for u, v in zip(path[:-1], path[1:])]) for path in paths]
    sequence = choose_best(s) + "A"
    r = translate_seq(sequence, n)
    return r


def run(lines, n):
    result = 0
    for line in lines:
        length = 0
        start = "A"
        for c in line:
            length += tanslate_digit(start, c, n)
            start = c
        result += length * int(line[:-1])
    return result


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)

start1 = time.time()
result1 = run(data, 2)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run(data, 25)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
