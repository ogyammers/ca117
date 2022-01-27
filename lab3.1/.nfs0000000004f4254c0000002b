#!/usr/bin/env python3

import sys

def primes(numbers):
   return [n for n in numbers if all(n % i != 0 for i in range(2,n))]

lines = sys.stdin.readlines()

for n in lines:
   numbers = [i for i in range(2, int(n) + 1)]
   print(f'Primes: {primes(numbers)}')
