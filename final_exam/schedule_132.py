#!/usr/bin/env python3

import sys

def change(t):
   hour, rest = (t.split(':'))
   hour = str(int(hour) + 12)
   t = hour + ':' + rest
   return t

def main():
   lines = [line.strip() for line in sys.stdin]
   am = []
   pm = []
   am12 = []
   pm12 = []

   for t in lines:
      if t[0:2] == '12':
         if 'a.m.' in t:
            am12.append(t)
      if t[0:2] == '12':
         if 'p.m.' in t:
            pm12.append(t)
      elif 'a.m.' in t:
         am.append(t)
      elif 'p.m.' in t:
         pm.append((t))

   for t in sorted(am12, key=change):
      print(t)
   for t in sorted(am, key=change):
      print(t)
   for t in sorted(pm12, key=change):
      print(t)
   for t in sorted(pm, key=change):
      print(t)


if __name__ == '__main__':
   main()
