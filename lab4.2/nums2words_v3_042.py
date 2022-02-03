#!/usr/bin/env python3

import sys

numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three',
           '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
           '8': 'eight', '9': 'nine', '10': 'ten'}

with open(sys.argv[1], 'r') as f:
   irish = {line.split()[0]: line.split()[1] for line in f}

mapped = [[irish[numbers[n]] for n in line.split()] for line in sys.stdin]

for line in mapped:
   print(' '.join(line))
