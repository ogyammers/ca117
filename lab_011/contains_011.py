#!/usr/bin/env python3

import sys

def contain(s):
   first = s.split()[0].lower()
   second = s.split()[1].lower()
   for c in first:
      if c in second:
         second = second.replace(c, "", 1)
      else:
         return "False"
   return "True"


for line in sys.stdin:
   s = line.strip()
   print(contain(s))
