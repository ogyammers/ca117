#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

n = int(lines[0])
buckets = list(map(int, lines[1].split()))

count = 0

i = 0
while count < n + 1 and i < len(buckets):
   count = count + buckets[i]
   i = i + 1

if count < n:
   print(len(buckets))
elif count == i:
   print(count)
else:
   print(i - 1)
