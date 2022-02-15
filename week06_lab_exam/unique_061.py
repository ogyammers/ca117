#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

def main():
   for line in lines:
      line = list(map(int, line.split()))
      unique = [n for n in line if line.count(n) < 2]
      if unique != []:
         print(sorted(unique)[-1])
      else:
         print('none')


if __name__ == '__main__':
   main()
