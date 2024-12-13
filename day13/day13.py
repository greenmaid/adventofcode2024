#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> str:
    with open(path, 'r') as f:
        data = f.read()
    return data

class Arcade():
    def __init__(self, xa, ya, xb, yb, targetX, targetY):
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb
        self.targetX = targetX
        self.targetY = targetY

    def __repr__(self):
        return f"ButtonA: ({self.xa},{self.ya}) ButtonB: ({self.xb},{self.yb}) Target ({self.targetX},{self.targetY})"

    def solve(self, limit=True):
        m = self
        if (m.xb * m.ya) == (m.xa * m.yb):
            return None
        pressA = ((m.xb * m.targetY) - (m.yb * m.targetX)) / ((m.xb * m.ya) - (m.xa * m.yb))
        pressB = (m.targetX - (pressA * m.xa)) / m.xb
        if pressA.is_integer() and pressA.is_integer():
            if limit and (pressA > 100 or pressB > 100):
                return None

            # check float approximations did not make some errors...
            if m.xa * int(pressA) + m.xb * int(pressB) != m.targetX:
                return None
            if m.ya * int(pressA) + m.yb * int(pressB) != m.targetY:
                return None

            return int(pressA), int(pressB)


def parse_data(data):
    arcades = []
    for machines_descr in data[:-1].split("\n\n"):
        match machines_descr.replace("=", " ").replace("+", " ").replace("\n", " ").replace(",", " ").split(" "):
            case ['Button', 'A:', 'X', xa, '', 'Y', ya, 'Button', 'B:', 'X', xb, '', 'Y', yb, 'Prize:', 'X', targetX, '', 'Y', targetY]:
                arcade = Arcade(
                    xa=int(xa),
                    ya=int(ya),
                    xb=int(xb),
                    yb=int(yb),
                    targetX=int(targetX),
                    targetY=int(targetY),
                )
                arcades.append(arcade)
    return arcades

# =========================================

def run1(arcades):
    result = 0
    for a in arcades:
        r = a.solve()
        if r:
            result += r[0] * 3  + r[1]
    return result

# =========================================

def run2(arcades):
    result = 0
    for a in arcades:
        a.targetX += 10000000000000
        a.targetY += 10000000000000
        r = a.solve(limit=False)
        if r:
            result += r[0] * 3  + r[1]
    return result


INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
arcades = parse_data(data)

start1 = time.time()
result1 = run1(arcades)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(arcades)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
