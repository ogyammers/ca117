#!/usr/bin/env python3

import sys

def sum_factors(n):
   factors = [i for i in range(1, n // 2 + 1) if n % i == 0]
   return sum(factors)


def is_perfect(n):
   return n == sum_factors(n)


def main():
   for n in [int(line) for line in sys.stdin]:
      print(is_perfect(n))


if __name__ == '__main__':
   main()
