#!/usr/bin/env python3

class Triathlete(object):
   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

   def add_time(self, disc, time):
      if disc == 'swim':
         self.swim = time
      if disc == 'cycle':
         self.cycle = time
      if disc == 'run':
         self.run = time

   def get_time(self, disc):
      if disc == 'swim':
         return self.swim
      if disc == 'cycle':
         return self.cycle
      if disc == 'run':
         return self.run

   def __eq__(self, other):
      return (self.swim + self.cycle + self.run) == (other.swim + other.cycle + other.run)

   def __lt__(self, other):
      return (self.swim + self.cycle + self.run) < (other.swim + other.cycle + other.run)

   def __gt__(self, other):
      return (self.swim + self.cycle + self.run) > (other.swim + other.cycle + other.run)

   def __str__(self):
      return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.swim + self.cycle + self.run}'

class Triathlon(object):
   def __init__(self):
      self.d = {}

   def add(self, t):
      self.d[t.tid] = t

   def lookup(self, t):
      if t in self.d:
         return self.d[t]

   def remove(self, t):
      if t in self.d:
         del self.d[t]
