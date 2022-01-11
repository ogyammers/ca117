#!/usr/bin/env python3

import sys

def sub(s):
   first = s.split()[0].lower()
   second = s.split()[1].lower()
   if first in second:
      return "True"
   else:
      return "False"


for line in sys.stdin:
   s = line.strip()
   subset = sub(s)
   print(subset)
