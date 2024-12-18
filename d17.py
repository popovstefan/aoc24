import math
import os

from utils import read_puzzle_input

pwd = os.path.dirname(__file__)

# read input
puzzle_input = read_puzzle_input(os.path.join(pwd, "puzzle_inputd17.txt"))

print(puzzle_input)

rega = int(puzzle_input[0].split("Register A:")[1].strip())
regb = int(puzzle_input[1].split("Register B:")[1].strip())
regc = int(puzzle_input[2].split("Register C:")[1].strip())

prgrm = [int(x.strip()) for x in puzzle_input[4].split("Program:")[1].split(",")]


def get_combo_operands():
    global rega, regb, regc
    return {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: rega,
        5: regb,
        6: regc,
        7: 7
    }


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def adv(var):
    global rega
    val = rega // (2 ** get_combo_operands()[var])
    rega = val
    return val


def bxl(var):
    global regb
    val = regb ^ var
    regb = val
    return val


def bst(var):
    global regb
    val = get_combo_operands()[var] % 8
    regb = val
    return val


def jnz(var):
    global rega
    if rega != 0:
        return var


def bxc(_):
    global regb, regc
    val = regb ^ regc
    regb = val
    return val


def out(var):
    return get_combo_operands()[var] % 8


def bdv(var):
    global rega, regb
    val = rega // 2 ** get_combo_operands()[var]
    regb = val
    return val


def cdv(var):
    global rega, regc
    val = rega // 2 ** get_combo_operands()[var]
    regc = val
    return val


opcodes = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}


def p1(pm):
    global rega
    ip = 0
    result = []
    while ip < len(pm):
        res = opcodes[pm[ip]](pm[ip + 1])
        # print("ip", ip, "res", res, "pm[ip]", pm[ip], "arg", pm[ip + 1])
        if pm[ip] == 3 and rega != 0:
            ip = pm[ip + 1]
        elif pm[ip] == 5:
            result.append(res)
            ip += 2
        else:
            ip += 2
    # print(",".join([str(x) for x in result]))
    return result


# print(prgrm)

# p1(prgrm)
# print(rega, regb, regc)


def p2(pm):
    global rega
    y_true = ",".join([str(x) for x in p1(pm)])
    print(y_true)
    for i in range(2):
        pass


p2(prgrm)
