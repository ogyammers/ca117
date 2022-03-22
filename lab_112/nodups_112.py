#!/usr/bin/env python3

import sys

def replace(line, seen):
   output = []
   for word in line.split():
      tmp = ''.join(c for c in word.lower() if c.isalnum())
      if tmp not in seen:
         seen.append(tmp)
         output.append(word)
      else:
         seen.append('.')
         output.append('.')
   return ' '.join(output), seen


def main():
   seen = []
   lines = [line.strip() for line in sys.stdin]
   for line in lines:
      print(replace(line, seen)[0])


if __name__ == '__main__':
   main()
