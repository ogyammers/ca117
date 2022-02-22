#!/usr/bin/env python3

import sys
lines = [line.strip().split() for line in sys.stdin]

def calc(line, d):
   total = d[line[0]]
   for i in range(len(line)):
      try:
         if line[i] == '+':
            total = total + d[line[i + 1]]
         elif line[i] == '-':
            total = total - d[line[i + 1]]
      except KeyError:
         return 'unknown'
   for k, v in d.items():
      if v == total:
         line = ' '.join(line)
         return k
   return 'unknown'


def main():
   d = {}
   for line in lines:
      if line[0] == 'clear':
         d.clear()
      if line[0] == 'def':
         d[line[1]] = int(line[2])
      if line[0] == 'calc':
         print(f'{" ".join(line[1:])} {calc(line[1:], d)}')


if __name__ == '__main__':
   main()
