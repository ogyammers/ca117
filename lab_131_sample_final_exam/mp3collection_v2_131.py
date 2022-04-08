class MP3Track(object):
   def __init__(self, title, duration, artist):
      self.title = title
      self.duration = duration
      self.artist = ', '.join(artist)

   def __str__(self):
      return f'Title: {self.title}\nBy: {self.artist}\nDuration: {self.duration}'

class MP3Collection(object):
   def __init__(self):
      self.d = {}

   def add(self, mp3):
      self.d[mp3.title] = mp3

   def remove(self, mp3):
      if mp3 in self.d:
         del self.d[mp3]

   def lookup(self, mp3):
      if mp3 in self.d:
         return self.d[mp3]
      return None

   def get_mp3s_by_artist(self, artist):
      tracklist = []
      for mp3 in self.d.values():
         if artist in mp3.artist:
            tracklist.append(mp3)
      return tracklist
