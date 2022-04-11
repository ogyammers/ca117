#!/usr/bin/env python3

import sys

def main():
   nums = [int(v) for v in sys.stdin.read().split()]
   x = nums[0]
   y = nums[1]
   n = nums[2]
   for i in range(1, n + 1):
      if i % x == 0 and i % y == 0:
         print('fizzbuzz')
      elif i % x == 0:
         print('fizz')
      elif i % y == 0:
         print('buzz')
      else:
         print(i)


if __name__ == '__main__':
   main()
