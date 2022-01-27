#!/usr/bin/env python3

import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
   censor = f.readlines()

censor = [line.strip() for line in censor]
lines = [line for line in sys.stdin]

for word in censor:
   lines = ([line.replace(word, len(word) * '@') for line in lines])

for line in lines:
   print(line.strip())
