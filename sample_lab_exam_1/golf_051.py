#!/usr/bin/env python3

import sys

lines = [line.strip().split() for line in sys.stdin]

def values(item):
   return item[1]

def scores(lines):
   scorecard = {}
   disqualified = []
   for line in lines:
      try:
         scorecard[' '.join(line[:-3])] = int(line[-3])  + int(line[-2]) + int(line[-1])
      except ValueError:
         disqualified.append(' '.join(line[:-3]))
   return scorecard, ', '.join(disqualified)

scorecard, disqualified = scores(lines)

for k, v in sorted(scorecard.items(), key=values):
   print(f'{k}: {v}')
if disqualified != '':
   print(f'Disqualified: {disqualified}')
