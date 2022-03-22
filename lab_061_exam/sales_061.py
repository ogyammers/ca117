#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]


def values(item):
   return item[1]


def table(line):
   d = {}
   for line in lines:
      name, values = line.split(':')
      values = list(map(int, values.split(',')))
      values = sum(values) / len(values)
      try:
         d[name] = values
      except ValueError:
         continue
   return d


def main():
      sales = table(lines)
      for k, v in sorted(sales.items(), key=values, reverse=True):
         print(f'{k}: {v:.2f}')


if __name__ == '__main__':
   main()
