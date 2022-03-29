class Student(object):
   def __init__(self, name, cao):
      self.name = name
      self.cao = cao

   def __str__(self):
      return f'Name: {self.name}\nCAO: {self.cao}'

def sorter(value):
   return value.cao

class Classlist(object):
   def __init__(self):
      self.d = {}

   def add(self, student):
      self.d[student.cao] = student

   def remove(self, cao):
      if cao in self.d:
         del self.d[cao]

   def lookup(self, cao):
      if cao in self.d:
         return self.d[cao]
      return None

   def __str__(self):
      cao_order = [f'{v}' for v in sorted(self.d.values(), key=sorter)]
      return '\n'.join(cao_order)
