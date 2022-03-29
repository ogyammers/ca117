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

   def race_time(self):
      return (self.swim + self.run + self.cycle)

   def __eq__(self, other):
      return (Triathlete.race_time(self)) == (Triathlete.race_time(other))

   def __lt__(self, other):
      return (Triathlete.race_time(self)) < (Triathlete.race_time(other))
   
   def __gt__(self, other):
      return (Triathlete.race_time(self)) > (Triathlete.race_time(other))

   def __str__(self):
      return f'Name: {self.name}\nID: {self.tid}\nRace time: {Triathlete.race_time(self)}'

class Triathlon(object):
   def __init__(self):
      self.d = {}

   def add(self, triathlete):
      self.d[triathlete.tid] = triathlete

   def remove(self, triatlete):
      del self.d[triathlete]
   
   def lookup(self, tid):
      return self.d[tid] if tid in self.d else None

   def values(item):
      return item.name

   def times(item):
      return item[1].swim + item[1].cycle + item[1].run

   def best(self):
      return min(self.d.values())

   def worst(self):
      return max(self.d.values())

   def __str__(self):
      return '\n'.join([f'Name: {v.name}\nID: {v.tid}' for v in sorted(self.d.values(), key=Triathlon.values)])
