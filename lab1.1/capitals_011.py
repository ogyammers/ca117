#!/usr/bin/env python3

import sys

def capital(s):
   if len(s) > 1:
      return s[0].capitalize() + s[1:len(s) - 1] + s[-1].capitalize()
   else:
      return s


for line in sys.stdin:
   s = line.strip()
   caps = capital(s)
   if len(caps) > 1:
      print(caps)
