#!/usr/bin/env python3

import sys

def capitalize(s):
   words = s.split()
   for i in range(len(words)):
      if words[i].startswith("m"):
         words[i] = words[i].capitalize()
         return " ".join(words)
   return s


for line in sys.stdin:
   s = line.strip()
   print(capitalize(s))
