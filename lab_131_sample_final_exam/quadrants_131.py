#!/usr/bin/env python3

import sys

def quadrant(point):
   x = int(point[0])
   y = int(point[1])
   if x > 0 and y > 0:
      return 1
   if x > 0 and y < 0:
      return 4
   if x < 0 and y > 0:
      return 2
   if x < 0 and y < 0:
      return 3
   return None


def main():
   lines = [line.strip().split() for line in sys.stdin]
   for line in lines:
      print(quadrant(line))


if __name__ == '__main__':
   main()
