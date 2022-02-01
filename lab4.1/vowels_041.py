#!/usr/bin/env python3

import sys

letters = sys.stdin.read().lower()
vowels = ['a', 'e', 'i', 'o', 'u']
d = {}

def count(letters):
   for c in vowels:
      d[c] = letters.count(c)
   return sorted(d.items(), key=lambda x: x[1], reverse=True)


w = 0
for i in range(len(vowels)):
   k, v = count(letters)[i]
   if w < len(str(v)):
      w = len(str(v))


for i in range(len(vowels)):
   k, v = count(letters)[i]
   print(f'{k} : {v: >{w}}')
