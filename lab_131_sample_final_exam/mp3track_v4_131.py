#!/usr/bin/env python3

def secs2mins(seconds):
   mins = seconds // 60
   secs = seconds % 60
   return f'{mins}:{secs:>02d}'


class MP3Track(object):
   def __init__(self, title, duration, artist=None):
      self.title = title
      self.duration = duration
      if artist is None:
         self.artist = []
      else:
         self.artist = artist

   def add_artist(self, artist):
      self.artist.append(artist)

   def __str__(self):
      return f'Title: {self.title}\nBy: {", ".join(self.artist)}\nDuration: {secs2mins(self.duration)}'
