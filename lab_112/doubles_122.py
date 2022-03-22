#!/usr/bin/env python3

import sys

def values(item):
   return item[1]


def doubles(word):
   count = 0
   doubles = ['aa', 'ee', 'ii', 'oo', 'uu']
   for i in range(0, len(word) - 1):
      if (word[i] + word[i + 1]) in doubles:
         count = count + 1
         i = i + 2
   return count


def main():
   lines = [line.strip() for line in sys.stdin]
   d = {}
   for line in lines:
      d[line] = doubles(line)
   d = sorted(d.items(), key=values)
   print(d[-1][0])


if __name__ == '__main__':
   main()
