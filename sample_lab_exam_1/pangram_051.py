#!/usr/bin/env python3

import sys

lines = [line.strip().lower() for line in sys.stdin]

def pangram(line):
   alpha = 'abcdefghijklmnopqrstuvwyxz'
   if (set(alpha) & set(line)) == set(alpha):
      return 'pangram'

   missing = ''.join(sorted(set(alpha) - set(line)))
   return (f'missing {missing}')


def main():
   for line in lines:
      print(pangram(line))


if __name__ == '__main__':
   main()
