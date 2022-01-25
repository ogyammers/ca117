#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
   anums = f.readlines()
with open(sys.argv[2], "r") as g:
   bnums = g.readlines()

for i in range(len(anums)):
   print(f'{anums[i].strip()}\n{bnums[i].strip()}')
