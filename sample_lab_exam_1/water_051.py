#!/usr/bin/env python3

import sys

n, buckets = [line.strip() for line in sys.stdin]
buckets = list(map(int, buckets.split()))
n = int(n)

total = 0
i = 0
while total <= n:
   total = total + buckets[i]
   i = i + 1

print(i - 1)
