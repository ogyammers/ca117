#!/usr/bin/env python3

import sys

def multiples_3(numbers):
   return [n for n in numbers if not n % 3]


def multiples_3_squared(numbers):
   return [n * n for n in numbers if not n % 3]


def multiples_4_doubled(numbers):
   return [n * 2 for n in numbers if not n % 4]


def multiples_3_or_4(numbers):
   return [n for n in numbers if not (n % 4) or not (n % 3)]


def multiples_3_and_4(numbers):
   return [n for n in numbers if not (n % 4) and not (n % 3)]


for line in sys.stdin:
   numbers = [i for i in range(1, int(line) + 1)]

   print(f'Multiples of 3: {multiples_3(numbers)}')
   print(f'Multiples of 3 squared: {multiples_3_squared(numbers)}')
   print(f'Multiples of 4 doubled: {multiples_4_doubled(numbers)}')
   print(f'Multiples of 3 or 4: {multiples_3_or_4(numbers)}')
   print(f'Multiples of 3 and 4: {multiples_3_and_4(numbers)}')
