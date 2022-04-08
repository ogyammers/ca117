class MP3Track(object):
   def __init__(self, title, duration, artist):
      self.title = title
      self.duration = duration
      self.artist = ', '.join(artist)

   def __str__(self):
      return f'Title: {self.title}\nBy: {self.artist}\nDuration: {self.duration}'
