#!/usr/bin/env python3

import sys
import re

def main():
   pattern = ''.join(['.' if c == '-' else c for c in sys.stdin.readline().strip()])
   string = ' '.join([word.strip() for word in sys.stdin.read().split() if len(word) == len(pattern)])

   if pattern == len(pattern) * '.':
      print(', '.join(string.split()))

   else:
      result = re.findall(pattern, string)

      if result != []:
         print(', '.join(result))


if __name__ == '__main__':
   main()
