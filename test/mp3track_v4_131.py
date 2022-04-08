class MP3Track(object):

    def __init__(self, title, duration, artists=None):
        self.title = title
        self.duration = duration
        if artists is None:
            artists = []
        self.artists = artists

    def add_artist(self, artist):
        self.artists.append(artist)

    def __str__(self):
        mins, secs = to_mins_seconds(self.duration)
        rl = []
        rl.append('Title: {}'.format(self.title))
        rl.append('By: {}'.format(', '.join(self.artists)))
        rl.append('Duration: {:01d}:{:02d}'.format(mins, secs))
        return '\n'.join(rl)

def to_mins_seconds(seconds):
    mins, secs = divmod(seconds, 60)
    return mins, secs
