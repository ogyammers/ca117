#!/usr/bin/env python3

import sys
line = sys.stdin.read().strip()

def clean(num):
    numS = str(num)
    cleared = ""
    for num in numS:
        if num != "0":
            cleared = cleared + num
    return int(cleared)

def mult(num):
    num = str(num)
    nums = []
    for n in num:
        nums.append(n)
    return eval("*".join(nums))

while 9 < int(line):
    if "0" in str(line):
        line = clean(line)
    else:
        line = mult(line)
print(line)
