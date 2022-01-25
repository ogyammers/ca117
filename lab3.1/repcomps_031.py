#!/usr/bin/env python3

import sys

def multiples_3(numbers):
   return ['X' if not n % 3 else n for n in numbers]


lines = sys.stdin.readlines()

for n in lines:
   numbers = [i for i in range(1, int(n) + 1)]
   print(f'Multiples of 3 replaced: {multiples_3(numbers)}')
