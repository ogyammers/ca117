#!/usr/bin/env python3

import sys

def palindrome(s):
   s = s.lower()
   forwards = ""
   backwards = ""
   i = 0
   while i < len(s):
      if s[i].islower() or s[i].isdigit():
         forwards = forwards + s[i]
         backwards = s[i] + backwards
      i = i + 1
   return forwards == backwards


for line in sys.stdin:
   print(palindrome(line.strip()))
