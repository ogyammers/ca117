#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()


def length(s):
   length = 0
   for line in lines:
      if len(line) > length:
         length = len(line)
   return length


for line in lines:
   print(f'{line.strip(): ^{(length(lines)) - 1}}')
