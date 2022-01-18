#!/usr/bin/env python3

import sys
import string

def punctuation(s):
   for i in s:
      if i in string.punctuation:
         s = s.replace(i, "")
   return s.lower().split()


def count(s):
   output = []
   for word in s:
      if word not in output:
         output.append(word)
   return len(output)


words = sys.stdin.read()
words = (punctuation(words))
print(count(words))
