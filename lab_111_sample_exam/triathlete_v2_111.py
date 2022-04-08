#!/usr/bin/env python3

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
