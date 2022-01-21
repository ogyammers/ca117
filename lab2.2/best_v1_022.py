#!/usr/bin/env python3

import sys

filename = sys.argv[1]

try:
   with open(filename, 'r') as f:
      best_mark = 0
      for line in f:
         [mark, student] = line.strip().split(' ', 1)
         if int(mark) > best_mark:
            best_mark, best_student = int(mark), student
      print(f'Best student: {best_student}\nBest mark: {best_mark}')

except ValueError:
   print(f'Invalid mark {line.split()[0]} encountered. Exiting.')
except FileNotFoundError:
   print(f'The file {filename} does not exist.')
