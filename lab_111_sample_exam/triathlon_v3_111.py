#!/usr/bin/env python3

def sorter(value):
   return Triathlete.total_time(value)

class Triathlete(object):
   def __init__(self, name, tid):
      self.name = name
      self.tid = tid
      self.d = {}

   def __str__(self):
      return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.total_time()}'

   def add_time(self, disc, time):
      self.d[disc] = time

   def get_time(self, disc):
      return self.d[disc]

   def total_time(self):
      return sum(self.d.values())

   def __eq__(self, other):
      return self.total_time() == other.total_time()

   def __lt__(self, other):
      return self.total_time() < other.total_time()

   def __gt__(self, other):
      return self.total_time() > other.total_time()

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
      return None

   def __str__(self):
      alpha_order = [f'{v}' for v in sorted(self.d.values(), key=sorter)]
      return '\n'.join(alpha_order)

   def best(self):
      return min(self.d.values())

   def worst(self):
      return max(self.d.values())
