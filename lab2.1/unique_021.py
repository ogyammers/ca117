#!/usr/bin/env python3

import sys
import string

def punctuation(s):
   for c in s:
      if c in string.punctuation:
         s = s.replace(c, "")
   return s.lower().split()


def count(s):
   output = []
   for word in s:
      if word not in output:
         output.append(word)
   return len(output)


print(count(punctuation(sys.stdin.read())))
