#!/usr/bin/env python3

import sys

def capitalize(s):
   i = 0
   while i < len(s) - 1 and s[i] != "m":
      i = i + 1
   if s[i] == "m" and s[i - 1] == " " or s[0] == "m":
      return s[:i] + "M" + s[i + 1:]
   else:
      return s


for line in sys.stdin:
   s = line.strip()
   cap = capitalize(s)
   print(cap)
