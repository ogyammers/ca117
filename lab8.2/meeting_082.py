#!/usr/bin/env python3

class Meeting(object):
   def __init__(self, h, m, d):
      self.hour = h
      self.minute = m
      self.duration = d

   def __str__(self):
      return f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)'
