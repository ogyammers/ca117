#!/usr/bin/env python3

import sys

def plural(s):
   f_fe = ["f", "fe"]
   vowel = ["a", "e", "i", "o", "u"]
   es = ["ch", "sh", "x", "s", "z"]

   if s.endswith("o"):
      return s + "es"

   if s.endswith("y") and s[-2] not in vowel:
      return s[:-1] + "ies"

   for i in range(len(es)):
      if s.endswith(es[i]):
         return s + "es"

   for i in range(len(f_fe)):
      if s.endswith(f_fe[i]):
         return s[:- len(f_fe[i])] + "ves"

   else:
      return s + "s"


for line in sys.stdin:
   print(plural(line.strip()))
