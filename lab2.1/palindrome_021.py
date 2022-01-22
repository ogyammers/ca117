#!/usr/bin/env python3

import sys

def palindrome(s):
   s = s.lower()
   for c in s:
      if not c.isalnum():
         s = s.replace(c, '')
   return s == s[::-1]


for line in sys.stdin:
   print(palindrome(line.strip()))
