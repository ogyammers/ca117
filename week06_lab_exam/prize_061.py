#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

def main():
   n = int(lines[0])
   s = lines[1]
   for c in s:
      if c == 'A' and n == 1:
         n = 2
      elif c == 'A' and n == 2:
         n = 1

      elif c == 'B' and n == 2:
         n = 3
      elif c == 'B' and n == 3:
         n = 2

      elif c == 'C' and n == 1:
         n = 3
      elif c == 'C' and n == 3:
         n = 1

   print(n)


if __name__ == '__main__':
   main()
