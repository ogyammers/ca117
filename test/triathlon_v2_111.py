class Triathlete(object):
   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

   def add_time(self, disc, time):
      if disc == 'swim':
         self.swim = time
      if disc == 'cycle':
         self.cycle = time
      if disc == 'run':
         self.run = time

   def get_time(self, disc):
      if disc == 'swim':
         return self.swim
      if disc == 'cycle':
         return self.cycle
      if disc == 'run':
         return self.run

   def __eq__(self, other):
      return (self.swim + self.run + self.cycle) == (other.swim + other.run + other.cycle)

   def __lt__(self, other):
      return (self.swim + self.run + self.cycle) < (other.swim + other.run + other.cycle)

   def __gt__(self, other):
      return (self.swim + self.run + self.cycle) > (other.swim + other.run + other.cycle)

   def __str__(self):
      return f'Name: {self.name}\nID: {self.tid}'

class Triathlon(object):
   def __init__(self):
      self.d = {}

   def add(self, t):
      self.d[t.tid] = t

   def remove(self, t):
      del self.d[t]
   
   def lookup(self, tid):
      return self.d[tid] if tid in self.d else None

   def values(item):
      return item[1].name

   def __str__(self):
      output = []
      for k, v in sorted(self.d.items(), key=Triathlon.values):
         output.append(f'Name: {v.name}\nID: {v.tid}')
      return '\n'.join(output)
