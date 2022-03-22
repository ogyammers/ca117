#!/usr/bin/env python3

import sys

def words_17(lines):
   return [word for word in lines if len(word) == 17]


def words_18(lines):
   return [word for word in lines if len(word) >= 18]


def cie(lines):
   return [word for word in lines if 'cie' in word]


def four_a(lines):
   return [line for line in lines if
           len([c for c in line.lower() if c == 'a']) == 4]


def two_q(lines):
   return [line for line in lines if
           len([c for c in line.lower() if c == 'q']) >= 2]


def angle(lines):
   return [line for line in lines if
           sorted(line.lower()) == sorted('angle') and not line == 'angle']


lines = [line.strip() for line in sys.stdin]

print(f'Words containing 17 letters: {words_17(lines)}')
print(f'Words containing 18+ letters: {words_18(lines)}')
print(f"Words with 4 a's: {four_a(lines)}")
print(f"Words with 2+ q's: {two_q(lines)}")
print(f'Words containing cie: {cie(lines)}')
print(f'Anagrams of angle: {angle(lines)}')
