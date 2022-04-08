#!/usr/bin/env python3

import sys

def quadrant(line):
   x, y = [int(v) for v in line.split()]
   if x > 0 and y > 0:
      return 1
   if x > 0 and y < 0:
      return 2
   if x < 0 and y < 0:
      return 3
   if x < 0 and y > 0:
      return 4


def main():
   lines = [line for line in sys.stdin]
   for line in lines:
      print(quadrant(line))


if __name__ == '__main__':
   main()
