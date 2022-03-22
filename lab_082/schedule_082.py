#!/usr/bin/env python3

class Meeting(object):
   def __init__(self, h, m, d):
      self.hour = h
      self.minute = m
      self.duration = d

   def __str__(self):
      return f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)'

class Schedule(object):
   def __init__(self):
      self.meetings = []

   def add(self, m):
      self.meetings.append(m)

   def __str__(self):
      schedule_list = [str(m) for m in self.meetings]
      schedule_list.append(f'Meetings today: {len(schedule_list)}')
      return '\n'.join(['Schedule', '--------'] + sorted(schedule_list))
