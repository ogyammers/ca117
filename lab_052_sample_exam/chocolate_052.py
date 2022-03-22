#!/usr/bin/env python3

import sys

bar = 400

def calories(line):
   if line < bar:
      return 1
   return line // bar


def main():
   lines = [int(line) for line in sys.stdin]
   for line in lines:
      print(calories(line))


if __name__ == '__main__':
   main()
