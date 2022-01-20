#!/usr/bin/env python3

import sys

filename = sys.argv[1]

highest = 0

try:
   with open(filename, "r") as f:

      for line in f:
         if int(line.split()[0]) > highest:
            highest = int(line.split()[0])
            student = line.split()[1:]
            mark = line.split()[0]
      print("Best student:", " ".join(student))
      print("Best mark:", mark)

except ValueError:
   print(f'Invalid mark {line.split()[0]} encountered. Exiting.')
except FileNotFoundError:
   print(f'The file {filename} does not exist.')
