#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

total = 0
for line in lines:
    line = line.rstrip().split()
    a, b, c = line
    a = int(a)
    b = int(b)
    c = int(c)
    total = c - b - 1

print(total)
