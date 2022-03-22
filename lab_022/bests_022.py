#!/usr/bin/env python3

import sys

filename = sys.argv[1]

try:
   with open(filename, 'r') as f:
      best_mark = 0
      for line in f:
         [mark, student] = line.strip().split(' ', 1)
         try:
            if int(mark) > best_mark:
               best_mark, best_student = int(mark), [student]
            elif int(mark) == best_mark:
               best_student.append(student)
         except ValueError:
            print(f'Invalid mark {mark} encountered. Skipping.')
      print(f'Best student(s): {", ".join(best_student)}\nBest mark: {best_mark}')
except FileNotFoundError:
   print(f'The file {filename} does not exist.')
