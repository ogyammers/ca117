#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
clubs = []
length = 0

for line in lines:
   club = (" ".join(line.strip().split()[1:-8]))
   if len(club) > length:
      length = len(club)

print(f'{"POS":>3} {"CLUB":<{length}} {"P":>2} {"W":>3} {"D":>3} {"L":>3} {"GF":>3} {"GA":>3} {"GD":>3} {"PTS":>3}')

for line in lines:
   line = (line.split())
   print(f'{line[0]:>3} {" ".join(line[1:-8]):<{length}} {line[-8]:>2} {line[-7]:>3} {line[-6]:>3} {line[-5]:>3} {line[-4]:>3} {line[-3]:>3} {line[-2]:>3} {line[-1]:>3}')
