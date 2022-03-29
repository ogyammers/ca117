#!/usr/bin/env python3

def sorter(value):
   return value.tid

class Triathlete(object):
   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

   def __str__(self):
      return f'Name: {self.name}\nID: {self.tid}'

class Triathlon(object):
   def __init__(self):
      self.d = {}

   def add(self, ath):
      self.d[ath.tid] = ath

   def remove(self, tid):
      if tid in self.d:
         del self.d[tid]

   def lookup(self, tid):
      if tid in self.d:
         return self.d[tid]
      else:
         return None

   def __str__(self):
      alpha_order = [f'{v}' for v in sorted(self.d.values(), key=sorter)]
      return '\n'.join(alpha_order)