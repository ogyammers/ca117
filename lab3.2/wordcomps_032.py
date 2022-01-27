#!/usr/bin/env python3

import sys

def aeiou(lines):
   words = [line for line in lines if
            sorted([c for c in line.lower() if c in 'aeiou']) == sorted('aeiou')]
   return min(words, key=len)


def iary(lines):
   return [line for line in lines if line[-4:] == 'iary']


def most_e(lines):
   most = max([((len(line) - len(line.replace("e", '')))) for line in lines])
   return [line for line in lines if
           (len(line) - len(line.replace('e', ''))) == most]


lines = [line.strip() for line in sys.stdin]

print(f'Shortest word containing all vowels: {aeiou(lines)}')
print(f'Words ending in iary: {len(iary(lines))}')
print(f"Words with most e's: {most_e(lines)}")
