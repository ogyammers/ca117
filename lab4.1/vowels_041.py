#!/usr/bin/env python3

import sys

letters = sys.stdin.read().lower()
vowels = ['a', 'e', 'i', 'o', 'u']

def count(letters):
   d = {}
   for c in vowels:
      d[c] = letters.count(c)
   return sorted(d.items(), key=lambda x: x[1], reverse=True)


freq = count(letters)
width = len(str(freq[0][1]))

for i in range(len(vowels)):
   key, value = freq[i]
   print(f'{key} : {value: >{width}}')
