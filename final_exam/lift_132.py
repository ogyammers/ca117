#!/usr/bin/env python3

import sys

def main():
   f, s, g, u, d = [int(line.strip()) for line in sys.stdin.read().split()]
   counter = 0
   while s != f and s <= g + d:
      if s + u <= f:
         s = s + u
         counter = counter + 1
      else:
         s = s - d
         counter = counter + 1

   if counter == 0:
      print('Sorry Sheila!')
   else:
      print(counter)


if __name__ == '__main__':
   main()
