#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

def values(item):
   return item[1]


def table(line):
   return {line.split(':')[0]: sum(list(map(int, line.split(':')[1].split(',')))) for line in lines}


def main():
      for k, v in sorted(table(lines).items(), key=values, reverse=True):
         print(f'{k}: {v:.2f}')


if __name__ == '__main__':
   main()
