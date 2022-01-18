#!/usr/bin/env python3

import sys

def anagram(s):
   [left, right] = s.split()
   if len(left) == len(right):
      for c in left:
         if c in right:
            right = right.replace(c, "", 1)
   return right == ""


for line in sys.stdin:
   print(anagram(line.strip()))
