#!/usr/bin/env python3

import sys


[numbers, order] = sys.stdin.readlines()
numbers = numbers.split()
numbers = list(map(int, numbers))
numbers.sort()

dic = {"A": numbers[0], "B": numbers[1], "C": numbers[2]}

print(dic[order[0]], dic[order[1]], dic[order[2]])
