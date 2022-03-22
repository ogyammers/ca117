#!/usr/bin/env python3

class Point(object):
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def midpoint(self, other):
      mid_x = (self.x + other.x) / 2
      mid_y = (self.y + other.y) / 2
      return Point(mid_x, mid_y)

   def __str__(self):
      return f'({self.x:.1f}, {self.y:.1f})'
