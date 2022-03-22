#!/usr/bin/env python3

class Score(object):

   def __init__(self, goals=None, points=None):
      if goals is None:
         self.goals = 0
      else:
         self.goals = goals
      if points is None:
         self.points = 0
      else:
         self.points = points

   def __str__(self):
      return f'{self.goals} goal(s) and {self.points} point(s)'
