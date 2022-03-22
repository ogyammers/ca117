#!/usr/bin/env python3

class Score(object):

   def __init__(self, goals=None, points=None):
      if points is None:
         self.points = 0
      else:
         self.points = points
      if goals is None:
         self.goals = 0
      else:
         self.goals = goals

   def __add__(self, other):
      tg = self.goals + other.goals
      tp = self.points + other.points
      return Score(tg, tp)

   def __iadd__(self, other):
      z = self + other
      self.goals, self.points = z.goals, z.points
      return self

   def __gt__(self, other):
      return (self.points + self.goals * 3) > (other.points + other.goals * 3)

   def __ge__(self, other):
      return (self.points + self.goals * 3) >= (other.points + other.goals * 3)

   def __lt__(self, other):
      return (self.points + self.goals * 3) < (other.points + other.goals * 3)

   def __le__(self, other):
      return (self.points + self.goals * 3) <= (other.points + other.goals * 3)

   def __eq__(self, other):
      return (self.points + self.goals * 3) == (other.points + other.goals * 3)

   def __ne__(self, other):
      return (self.points + self.goals * 3) != (other.points + other.goals * 3)

   def __str__(self):
      return f'{self.goals} goal(s) and {self.points} point(s)'
