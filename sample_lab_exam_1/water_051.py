#!/usr/bin/env python3

import sys

n, buckets = [line.strip() for line in sys.stdin]
n, buckets = int(n), list(map(int, buckets.split()))

def filled(n, buckets):
   total = 0
   i = 0
   while total <= n:
      total = total + buckets[i]
      i = i + 1
   return i - 1


def main():
   print(filled(n, buckets))


if __name__ == '__main__':
   main()
