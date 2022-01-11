#!/usr/bin/env python3

import sys

def middle(s):
   if len(s) // 2 != len(s) / 2:
      return s[len(s) // 2:(len(s) // 2) + 1]
   else:
      return "No middle character!"


for line in sys.stdin:
   s = line.strip()
   mid = middle(s)
   print(mid)
