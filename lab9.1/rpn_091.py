#!/usr/bin/env python3

from math import sqrt

class Stack(object):

   def __init__(self):
      self.list = []

   def push(self, e):
      self.list.append(e)

   def pop(self):
      return self.list.pop()

   def top(self):
      return self.list[-1]

   def is_empty(self):
      return len(self.list) == 0

   def __len__(self):
      return len(self.list)

def calculator(test):
   binops = {'+': float.__add__, '-': float.__sub__,
             '*': float.__mul__, '/': float.__truediv__}
   uniops = {'n': float.__neg__, 'r': sqrt}
   ops = '+-*/nr'
   s = Stack()
   for c in test.split():
      if c not in ops:
         s.push(float(c))
      elif c in binops:
         second, first = s.pop(), s.pop()
         s.push(binops[c](first, second))
      elif c in uniops:
         s.push(uniops[c](s.pop()))
   return s.top()
