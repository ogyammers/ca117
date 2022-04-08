#!/usr/bin/env python3

import sys

def price(line):
   prices = sorted([int(n) for n in line.split()], reverse=True)
   free = prices[2::3]
   return sum(prices) - sum(free)


def main():
   for line in sys.stdin:
      print(price(line.strip()))


if __name__ == '__main__':
   main()
