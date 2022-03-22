#!/usr/bin/env python3

import sys
import string

def convert(words):
   words = [word.lower().strip(string.punctuation) for word in words]
   return sorted(words)


def totals(words):
   d = {}
   for word in words:
      d[word] = words.count(word)
   return d


words = sys.stdin.read().split()

d = totals(convert(words))

for key in d:
   print(f'{key} : {d[key]}')
