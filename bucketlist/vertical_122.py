#!/usr/bin/env python3

import sys

def lower(word):
   return word.lower()


def rotate(words):
   new = ['' for c in words[0]]
   for word in words:
      for i in range(len(words[0])):
         new[i] = new[i] + word[i]
   return new


def main():
   lines = [line.strip() for line in sys.stdin]
   sorted_words = sorted(rotate(lines), key=lower)
   print('\n'.join(rotate(sorted_words)))


if __name__ == '__main__':
   main()
