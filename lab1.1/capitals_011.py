#!/usr/bin/env python3

import sys

def capitalize(s):
   if len(s) > 1:
      return s[0].upper() + s[1:-1] + s[-1].upper()
   else:
      return s


for line in sys.stdin:
   s = line.strip()
   caps = capitalize(s)
   if len(caps) > 1:
      print(caps)
