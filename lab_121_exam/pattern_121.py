#!/usr/bin/env python3

import sys

lines_in = [line.strip() for line in sys.stdin]
pattern = lines_in[0]
lines = lines_in[1:]
output = lines_in[1:]
matches = []

for i in range(len(pattern)):
   if pattern[i] == '-':
      for j in range(len(lines)):
         if len(lines[j]) == len(pattern):
            lines[j] = lines[j].replace(lines[j][i], '-', 1)

for i in range(len(lines)):
   if lines[i] == pattern:
      matches.append(output[i])

print(', '.join(matches))
