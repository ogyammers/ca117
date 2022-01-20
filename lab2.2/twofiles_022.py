#!/usr/bin/env python3

import sys

afile = sys.argv[1]
bfile = sys.argv[2]

with open(afile, "r") as f:
   anums = f.readlines()

with open(bfile, "r") as g:
   bnums = g.readlines()

i = 0
while i < len(anums):
   print(anums[i].strip())
   print(bnums[i].strip())
   i = i + 1
