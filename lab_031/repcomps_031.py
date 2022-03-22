#!/usr/bin/env python3

import sys

def multiples_3(numbers):
   return ['X' if not n % 3 else n for n in numbers]


for line in sys.stdin:
   numbers = [i for i in range(1, int(line) + 1)]
   print(f'Multiples of 3 replaced: {multiples_3(numbers)}')
