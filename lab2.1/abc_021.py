#!/usr/bin/env python3

import sys

nums, order = sys.stdin.readlines()
nums = list(map(int, nums.split()))
nums.sort()

d = {"A": nums[0], "B": nums[1], "C": nums[2]}

print(d[order[0]], d[order[1]], d[order[2]])
