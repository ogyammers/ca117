#!/usr/bin/env python3

import sys

def main():
   lines = [line.strip() for line in sys.stdin]
   a = []
   b = []
   for i in range(len(lines)):
      if i % 2 == 0:
         a.append(lines[i])
      else:
         b.insert(0, lines[i])

   for name in a + b:
      print(name)


if __name__ == '__main__':
   main()
