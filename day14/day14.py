#!/usr/bin/env python3

import os
import time
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse_data(lines):
    robots = []
    for line in lines:
        match line.replace("="," ").replace(",", " ").split(" "):
            case ['p', x, y, 'v', vx, vy]:
                robots.append({"x": int(x), "y": int(y), "vx": int(vx), "vy": int(vy)})
    return robots


# =========================================

def next_position(robot):
    robot["x"] = (robot["x"] + robot["vx"]) % LIMX
    robot["y"] = (robot["y"] + robot["vy"]) % LIMY


def get_safety_factor(robots):
    q1, q2, q3, q4 = 0, 0, 0, 0
    middleX = int(LIMX/2)
    middleY = int(LIMY/2)
    for r in robots:
        if r["x"] < middleX and r["y"] < middleY:
            q1 += 1
        elif r["x"] > middleX and r["y"] < middleY:
            q2 += 1
        elif r["x"] < middleX and r["y"] > middleY:
            q3 += 1
        elif r["x"] > middleX and r["y"] > middleY:
            q4 += 1
    return q1 * q2 * q3 * q4


def run1(robots):
    for _ in range(100):
        for i,r in enumerate(robots):
            next_position(r)
    return get_safety_factor(robots)

# =========================================


def display_robots(robots):
    msg = ""
    for y in range(LIMY):
        for x in range(LIMX):
            char = " "
            for r in robots:
                if r["x"] == x and r["y"] == y:
                    char = "#"
                    break
            msg += char
        msg += "\n"
    msg += "\n"
    return msg


def check_no_overlap(robots):
    """
    Check if some robot locations are overlapping
    """
    check = {}
    for r in robots:
        if (r["x"], r["y"]) in check:
            return False
        check[(r["x"], r["y"])] = True
    return True


def run2(robots):
    for i in range(101, 100000):   # robots moved 100x in the first step
        for j,r in enumerate(robots):
            next_position(r)
        if check_no_overlap(robots):
            # print(display_robots(robots))
            return i  


INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
robots = parse_data(data)

LIMX = 101
LIMY = 103

start1 = time.time()
result1 = run1(robots)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(robots)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
