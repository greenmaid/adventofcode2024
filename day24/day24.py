#!/usr/bin/env python3

import os
import time
from typing import List
from unittest import result
import random

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read()
    return lines



def parse_data(data):
    wire_values, gate_plug = data.split('\n\n')

    wires = {}
    for line in wire_values.split('\n'):
        wire, value = line.split(': ')
        wires[wire] = int(value)

    gates = {}
    for line in gate_plug.split('\n'):
        match line.split(' '):
            case [v1, op, v2, '->', val]:
                gates[val] = (v1, op, v2)

    return wires, gates

# =========================================


def evalutate(w, wires, gates):
    if w in wires:
        return wires[w], wires, gates
    v1, op, v2 = gates[w]
    v1, wires, gates = evalutate(v1, wires, gates)
    v2, wires, gates = evalutate(v2, wires, gates)
    res = -1
    match op:
        case 'AND':
            res = v1 & v2
        case 'OR':
            res = v1 | v2
        case 'XOR':
            res = v1 ^ v2
        case '_':
            raise ValueError(f"Unknown operator: {op}")
    wires[w] = res
    # print(f"{w} = {v1} {op} {v2} = {res}")
    return res, wires, gates

def resolve(wires, gates):
    for g in gates:
        _, wires, gates = evalutate(g, wires, gates)
    return wires


def run1(wires, gates):
    wires = resolve(wires, gates)
    i = 0
    result = 0
    while True:
        z = f"z{i:02d}"
        if z not in wires and z not in gates:
            break
        result += wires[z] * 2**i
        i += 1
    return result

# =========================================


def check(wires):
    i = 0
    errors = 0
    while True:
        x = f"x{i:02d}"
        y = f"y{i:02d}"
        z = f"z{i:02d}"
        if z not in wires:
            break
        if x not in wires:
            wires[x] = 0
        if y not in wires:
            wires[y] = 0
        if wires[x] & wires[y] != wires[z]:
            errors += 1
        i += 1
    return errors


def permute(a, b, gates):
    gates[a], gates[b] = gates[b], gates[a]
    return gates


def test_permuations(a, b, wires, gates):
    w1 = wires.copy()
    w2 = wires.copy()
    g = gates.copy()
    errors1 = check(resolve(w1, g))
    g = permute(a, b, g)
    try:
        errors2 = check(resolve(w2, g))
        if errors1 > errors2:
            return True, g, errors2
    except RecursionError:
        return False, gates, -1
    return False, gates, errors1


def run2(wires, gates):
    initial_wires = wires.copy()
    initial_gates = gates.copy()
    permutations = []

    while True:
        a, b = random.sample(sorted(gates), 2)
        if a in permutations or b in permutations:
            continue

        wires = initial_wires.copy()
        success, gates, errors = test_permuations(a, b, wires, gates)
        if success:
            permutations.append(a)
            permutations.append(b)
            print("Permutations: ", permutations, "Errors: ", errors)
            wires = initial_wires.copy()
            wires = resolve(wires, gates)
            if check(wires) == 0:
                break
        else:
            print("tested: ", (a,b), "Errors: ", errors, permutations)

INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
wires, gates = parse_data(data)

start1 = time.time()
result1 = run1(wires, gates)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
wires, gates = parse_data(data)
result2 = run2(wires, gates)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
