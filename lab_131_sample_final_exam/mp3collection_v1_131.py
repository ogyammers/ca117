#!/usr/bin/env python3

class MP3Track(object):
   def __init__(self, title, duration):
      self.title = title
      self.duration = duration

   def __str__(self):
      return f'Title: {self.title}\nDuration: {self.duration}'

class MP3Collection(object):
   def __init__(self):
      self.d = {}

   def add(self, mp3):
      self.d[mp3.title] = mp3

   def lookup(self, title):
      if title in self.d:
         return self.d[title]
      return None

   def remove(self, title):
      if title in self.d:
         del self.d[title]
