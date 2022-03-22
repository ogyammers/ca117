#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]
word = ['n', 'i', 'c', 'e']


def nice(line):
   for c in line:
      if c not in word:
         line = line.replace(c, '', 1)
   return line


def main():
   for line in lines:
      if sorted(nice(line)) == sorted('nice'):
         print(line)


if __name__ == '__main__':
   main()
