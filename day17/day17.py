#!/usr/bin/env python3

import os
import time

# =========================================

def combo(o, Registers):
    if o <= 3:
        return o
    if o == 4:
        return Registers["A"]
    if o == 5:
        return Registers["B"]
    if o == 6:
        return Registers["C"]


def execute(program, Registers):
    output = []
    idx = 0
    while idx < len(program):
        opcode = program[idx]
        o = program[idx+1]

        if opcode == 0:  # adv
            Registers["A"] = int(Registers["A"] / 2**combo(o, Registers))
            idx += 2
        if opcode == 1:  # bxl
            Registers["B"] = Registers["B"] ^ o
            idx += 2
        if opcode == 2:  # bst
            Registers["B"] = combo(o, Registers) % 8
            idx += 2
        if opcode == 3:  # jnz
            if Registers["A"] == 0:
                idx += 2
            else:
                idx = o
        if opcode == 4:  # bxc
            Registers["B"] = Registers["B"] ^ Registers["C"]
            idx += 2
        if opcode == 6:  # bdv
            Registers["B"] = int(Registers["A"] / 2**combo(o, Registers))
            idx += 2
        if opcode == 7:  # cdv
            Registers["C"] = int(Registers["A"]/2**combo(o, Registers))
            idx += 2
        if opcode == 5:  # out
            output.append(combo(o, Registers) % 8)
            # print(output, Registers)
            idx += 2
    return output


def run1(program):
    Registers = {
        "A" : 63687530,
        "B" : 0,
        "C" : 0,
    }
    output = execute(program, Registers)
    return ','.join([str(x) for x in output])

# =========================================

def run2(program):
    factors = [0] * len(program)
    factors[0] = 1
    while True:
        init = sum([ k*(8**i) for i,k in enumerate(reversed(factors))])
        Registers = {
            "A" : init,
            "B" : 0,
            "C" : 0,
        }
        output = execute(program, Registers)
        # print(factors, init, output)
        if output == program:
            break
        for i,v in enumerate(reversed(program)):
            if list(reversed(output))[i] != v:
                factors[i] += 1
                break
    return factors, init

# program = [0,3,5,4,3,0]
program = [2,4,1,3,7,5,0,3,1,5,4,1,5,5,3,0]

start1 = time.time()
result1 = run1(program)
duration1 = (time.time() - start1) * 1000
print("Result1 = ", result1, f"    \t(in {duration1:.6f}ms)")

start2 = time.time()
_, result2 = run2(program)
duration2 = (time.time() - start2) * 1000
print("Result2 = ", result2, f"    \t(in {duration2:.6f}ms)")
