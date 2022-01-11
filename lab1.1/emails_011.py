#!/usr/bin/env python3

import sys

def email(s):
   first = s.split(".")[0].capitalize()
   second = s.split(".")[1].split("@")[0].capitalize()
   surname = []
   for c in second:
      if not("0" <= c and c <= "9"):
         surname.append(c)
   return (first, "".join(surname))


for line in sys.stdin:
   s = line.strip()
   name = email(s)
   print(" ".join(name))
