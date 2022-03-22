#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

n = int(lines[0])
buckets = list(map(int, lines[1].split()))

count = 0

i = 0
while i < len(buckets) and count <= n:
   count = count + buckets[i]
   i = i + 1

if sum(buckets) < n:
   print(len(buckets))
else:
   print(i - 1)
