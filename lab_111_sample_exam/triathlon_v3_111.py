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

   def best(self):
      best = []
      for k, v in sorted(self.d.items(), key=lambda item: (item[1].swim + item[1].run + item[1].cycle)):
         best.append(f'Name: {v.name}\nID: {k}\nRace time: {v.swim + v.cycle + v.run}')
      return best[0]

   def worst(self):
      worst = []
      for k, v in sorted(self.d.items(), key=lambda item: item[1].swim):
         worst.append(f'Name: {v.name}\nID: {k}\nRace time: {v.swim + v.cycle + v.run}')
      return worst[-1]

   def __str__(self):
      output = []
      for k, v in sorted(self.d.items(), key=lambda item: item[1].name):
         output.append(f'Name: {v.name}\nID: {k}')
      return '\n'.join(output)
