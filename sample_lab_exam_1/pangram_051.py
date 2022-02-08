#!/usr/bin/env python3

import sys

lines = [line.strip().lower() for line in sys.stdin]
alpha = 'abcdefghijklmnopqrstuvwyxz'


def pangram(line):
   if (set(alpha) & set(line)) == set(alpha):
      return 'pangram'
   else:
      missing = ''.join(sorted(set(alpha) - set(line)))
      return (f'missing {missing}')


for line in lines:
   print(pangram(line))
