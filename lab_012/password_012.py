#!/usr/bin/env python3

import sys

def classes(s):
   digit = 0
   upper = 0
   lower = 0
   other = 0
   for c in line:
      if c.isdigit():
         digit = 1
      if c.isupper():
         upper = 1
      if c.islower():
         lower = 1
      if c in "!@#$%^&*()-+?_=,<>/":
         other = 1
   return(digit + upper + lower + other)


for line in sys.stdin:
   print(classes(line))
