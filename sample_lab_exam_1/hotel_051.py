#!/usr/bin/env python3

import sys

line = sys.stdin.readline()
rooms, occupied = line[0], line[1:]

available = [i for i in range(1, int(rooms)) if str(i) not in occupied]

if available == []:
   print('no room')
else:
   print(sorted(available)[0])
