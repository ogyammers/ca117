#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    missing = 'abcdefghijklmnopqrstuvwxyz'
    line = line.rstrip()
    for each in line:
        if each.lower() in missing:
            missing = missing.replace(each.lower(), '', 1)
    if not missing:
        print('pangram')
    else:
        print(f'missing {missing}')
