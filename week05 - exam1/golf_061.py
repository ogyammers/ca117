#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

d = {}
dis = []
for line in lines:
    try:
        line = line.strip().split()
        name = " ".join(line[:-3])
        shots = 0
        for each in line[-3:]:
            shots = shots + int(each)
        d[name] = shots
    except ValueError:
        check = 1
        dis.append(name)

ans = dict(sorted(d.items(), key=lambda item: item[1]))

for k, v in ans.items():
    print(f'{k}: {v}')
try:
    if check == 1:
        print(f'Disqualified: {", ".join(dis)}')
except NameError:
    pass
