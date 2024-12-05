#!/usr/bin/env python3

import os
import time
from typing import List
from functools import cmp_to_key

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input(path: str) -> str:
    with open(path, 'r') as f:
        data = f.read()
    return data

def parse_data(data):
    rules_data, print_data = data.split("\n\n")

    rules = {}
    for rule in rules_data.split("\n"):
        val1, val2 = rule.split("|")
        if int(val1) not in rules:
            rules[int(val1)] = []
        rules[int(val1)].append(int(val2))

    print_orders = []
    for order in print_data.split("\n"):
        pages = []
        if order:
            for p in order.split(","):
                pages.append(int(p))
            print_orders.append(pages)

    return rules, print_orders

# =========================================

def is_valid(order, rules):
    for i, p in enumerate(order):
        if p in rules:
            should_not_be_before = rules[p]
            for snbb in should_not_be_before:
                if snbb in order[:i]:
                    return False
    return True


def locate_error(order, rules):
    for i, p in enumerate(order):
        if p in rules:
            should_not_be_before = rules[p]
            for snbb in should_not_be_before:
                if snbb in order[:i]:
                    return i, order[:i].index(snbb)
    return -1, -1


def get_middle(order):
    return order[int((len(order)/2))]


def run1(rules, print_orders):
    result = 0
    for order in print_orders:
        if is_valid(order, rules):
            result += get_middle(order)
    return result

# =========================================

def get_correct_order_with_swaps(order, rules):
    new = order
    while not is_valid(new, rules):
        index1, index2 = locate_error(new, rules)
        new[index1], new[index2] = new[index2], new[index1]
    return new


def sort_order(order, rules):
    def custom_comp_fct(a,b):
        if a in rules and b in rules[a]:
                return -1
        return 0
    return sorted(order, key=cmp_to_key(custom_comp_fct))


def run2(rules, print_orders):
    result = 0
    for order in print_orders:
        if not is_valid(order, rules):
            # correct = get_correct_order_with_swaps(order, rules)  // first try, not so effective
            correct = sort_order(order, rules)
            result += get_middle(correct)
    return result


# INPUT = f"{SCRIPT_DIR}/input_test.txt"
INPUT = f"{SCRIPT_DIR}/input.txt"
data = read_input(INPUT)
rules, print_orders = parse_data(data)

start1 = time.time()
result1 = run1(rules, print_orders)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
result2 = run2(rules, print_orders)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
