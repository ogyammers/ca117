#!/usr/bin/env python3

import sys

filename = sys.argv[1]

highest = 0

try:
   with open(filename, "r") as f:

      for line in f:
         try:
            if int(line.split()[0]) > highest:
               highest = int(line.split()[0])
               mark = line.split()[0]
         except ValueError:
            print(f'Invalid mark {line.split()[0]} encountered. Skipping.')

except FileNotFoundError:
   print(f'The file {filename} does not exist.')

student = []

with open(filename, "r") as f:
   for line in f:
      if int(line.split()[0]) == int(mark):
         student.append(" ".join(line.split()[1:]))

print("Best student(s):", ", ".join(student))
print("Best mark:", mark)
