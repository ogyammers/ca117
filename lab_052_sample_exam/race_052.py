#!/usr/bin/env python3

import sys

def min2secs(time):
   return int(time.split(':')[0]) * 60 + int(time.split(':')[1])


def sec2mins(line):
   return (str(line // 60) + ':' + str(line % 60))


def best_runner(lines):
   best = []
   times = [line.split()[1:] for line in lines]
   for line in times:
      try:
         line = [min2secs(time) for time in line]
      except ValueError:
         continue
      best.append((min(line)))
   return sec2mins(min(best))


def main():
   lines = [line.strip() for line in sys.stdin]
   best_time = best_runner(lines)
   for line in lines:
      if best_time in line:
         print(f'{line.split()[0]} : {best_time}')


if __name__ == '__main__':
   main()
