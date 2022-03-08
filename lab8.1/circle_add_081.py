#!/usr/bin/env python3

class Point(object):
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def midpoint(self, other):
      mid_x = (self.x + other.x) / 2
      mid_y = (self.y + other.y) / 2
      return Point(mid_x, mid_y)

   def __str__(self):
      return f'({self.x:.1f}, {self.y:.1f})'

class Circle(object):
   def __init__(self, centre=None, radius=1):
      if centre is None:
         self.point = Point()
      else:
         self.point = centre
      self.centre = self.point
      self.radius = radius

   def __add__(self, other):
      r = self.radius + other.radius
      c = Point.midpoint(self.centre, other.centre)
      return Circle(c, r)

   def __str__(self):
      return f'Centre: {self.centre}\nRadius: {self.radius}'
