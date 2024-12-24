#!/usr/bin/env python3

import os
import time
import itertools
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse_data(lines):
    links = {}
    for line in lines:
        c1, c2 = line.split('-')
        if c1 not in links:
            links[c1] = []
        links[c1].append(c2)
        if c2 not in links:
            links[c2] = []
        links[c2].append(c1)

    return links

# =========================================

def run1(links):
    groups = []
    UNICITY = {}

    for c1, connected in links.items():
        couples = itertools.combinations(connected, 2)
        for c2, c3 in couples:
            if c2 in links[c3]:
                g = tuple(sorted([c1, c2, c3]))
                if g not in UNICITY:
                    groups.append(g)
                    UNICITY[g] = True

    filtered_groups = []
    for g in groups:
        for c in g:
            if c.startswith('t'):
                filtered_groups.append(g)
                break

    return len(filtered_groups)

# =========================================

def run2(links):
    group_length = max([len(v) for _,v in links.items()])

    largest = None
    while not largest:
        for c, connected in links.items():
            if len(connected) >= group_length:
                combis = itertools.combinations(connected, group_length)
                for combi in combis:
                    couples = itertools.combinations(combi, 2)
                    if all([c2 in links[c1] for c1,c2 in couples]):
                        largest = list(combi) + [c]
                        break
        group_length -= 1

    return ",".join([x for x in sorted(largest)])


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
links = parse_data(data)

start1 = time.time()
result1 = run1(links)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(links)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
