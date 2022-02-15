#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

a = lines[0].rstrip()
b = lines[1].rstrip()

i = 0
ans = []
while i < len(a):
    if a[i] == b[i]:
        ans.append('-')
    else:
        ans.append('*')
    i = i + 1

print(a)
print(b)
print(''.join(ans))
