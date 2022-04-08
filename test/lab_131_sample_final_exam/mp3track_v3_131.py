class MP3Track(object):
   def __init__(self, title, duration, artist=None):
      self.title = title
      self.duration = duration
      if artist is not None:
         self.artist = ', '.join(artist)
      else:
         self.artist = ''

   def __str__(self):
      return f'Title: {self.title}\nBy: {self.artist}\nDuration: {self.duration}'

   def add_artist(self, artist):
      if self.artist == '':
         self.artist = artist
      else:
         self.artist = self.artist + ', ' + artist
