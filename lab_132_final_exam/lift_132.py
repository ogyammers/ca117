#!/usr/bin/env python3

import sys


def main():
    f, s, g, u, d = [int(line.strip()) for line in sys.stdin.read().split()]

    counter = 0
    while s != g and counter <= 1000000:

        if s < g:
            s = s + u
            counter = counter + 1
        if s > g:
            s = s - d
            counter = counter + 1

    if s != g:
        print('Sorry Sheila!')
    else:
        print(counter)


if __name__ == '__main__':
    main()
