#!/usr/bin/env python3

import sys

def upper(line):
   for c in line:
      if c.islower():
         line = line.replace(c, '-')
   return (max(line.split('-')))

def main():
   lines = [line.strip() for line in sys.stdin]
   for line in lines:
      print(upper(line))


if __name__ == '__main__':
   main()
