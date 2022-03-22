#!/usr/bin/env python3

class Stack(object):

   def __init__(self):
      self.list = []

   def push(self, c):
      self.list.append(c)

   def pop(self):
      return self.list.pop()

   def top(self):
      return self.list[-1]

   def is_empty(self):
      return len(self.list) == 0

   def __len__(self):
      return len(self.list)

   def __str__(self):
      return ''.join(self.list)

def matcher(test):
   d = {')': '(', ']': '[', '}': '{'}
   lefties, righties = '([{', ')]}'
   if test[0] not in lefties:
     return False

   s = Stack()
   for c in test:
      if c in lefties:
         s.push(c)
      if c in righties:
         if d[c] != s.top():
            return False
         s.pop()
   return len(s) == 0
