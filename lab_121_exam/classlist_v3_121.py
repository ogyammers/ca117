class Student(object):
   def __init__(self, name, cao):
      self.name = name
      self.cao = cao
      self.d = {}

   def __str__(self):
      return f'Name: {self.name}\nCAO: {self.cao}'

   def add_grade(self, subject, grade):
      self.d[subject] = grade

   def get_grade(self, subject):
      if subject in self.d:
         return self.d[subject]
      return 'N/A'

def sorter(value):
   return value.cao

def popular():
   return Student.subjects

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

   def most_popular_subject(self):
      output = []
      most = {}
      for v in self.d.values():
         for s in v.d.keys():
            output.append(s)
      for s in output:
         if s in most:
            most[s] = most[s] + 1
         else:
            most[s] = 1
      return min(most)

   def __str__(self):
      cao_order = [f'{v}' for v in sorted(self.d.values(), key=sorter)]
      return '\n'.join(cao_order)
