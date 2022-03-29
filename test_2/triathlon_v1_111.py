#!/usr/bin/env python3

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