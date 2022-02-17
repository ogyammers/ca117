def overlap(x1=None, y1=None, r1=None, x2=None, y2=None, r2=None):
   xy = [x1, y1, x2, y2]
   xy = [0 if n is None else n for n in xy]
   r = [r1, r2]
   r = [1 if n is None else n for n in r]
   d = (xy[2] - xy[0]) ** 2 + (xy[3] - xy[1]) ** 2
   return d < ((r[0] + r[1]) ** 2)
