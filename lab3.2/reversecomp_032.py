#!/usr/bin/env python3

import sys

def binsearch(query, lines):
   low = 0
   high = len(lines) - 1
   while low <= high:
      mid = (low + high) // 2
      if lines[mid] < query:
         low = mid + 1
      elif lines[mid] > query:
         high = mid - 1
      else:
         return True
   return False


lines = [line.strip() for line in sys.stdin if len(line.strip()) > 4]
low = [line.lower() for line in lines]

print([line for line in lines if binsearch(line[::-1].lower(), low)])
