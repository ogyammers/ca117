#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    line = line.rstrip().split()
    a, b, c = line
    a = int(a)
    b = int(b)
    c = int(c)
    # print(a, b, c)
    if (a + b == c) or (a - b == c) or (b - a == c) or (a / b == c) or (b / a == c) or (a * b == c):
        print('yes')
    else:
        print('no')
