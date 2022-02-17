#!/usr/bin/env python3

import sys
from math import sqrt

lines = [[int(n) for n in line.strip().split()] for line in sys.stdin]

def roots(a, b, c):
   try:
      r1 = (- b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
      r2 = (- b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
   except ValueError:
      return None
   return (f'r1 = {r1}, r2 = {r2}')


def main():
   for line in lines:
      a, b, c = line
      print(roots(a, b, c))


if __name__ == '__main__':
   main()
