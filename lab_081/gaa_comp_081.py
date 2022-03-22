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
      return f'{self.points} goals(s) and {self.goals} point(s)'
