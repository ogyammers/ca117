#!/usr/bin/env python3

import sys

def decode(line):
   vowels = 'aeiou'
   string = ''
   i = 0
   while i < len(line):
      string = string + line[i]
      if line[i] in vowels:
         i = i + 2
      i = i + 1
   return string


def main():
   lines = [line.strip() for line in sys.stdin]
   for line in lines:
      print(decode(line))


if __name__ == '__main__':
   main()
