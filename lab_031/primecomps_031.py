#!/usr/bin/env python3

import sys

def primes(numbers):
   return [n for n in numbers if all(n % i != 0 for i in range(2, n))]


for line in sys.stdin:
   numbers = [i for i in range(2, int(line))]
   print(f'Primes: {primes(numbers)}')
