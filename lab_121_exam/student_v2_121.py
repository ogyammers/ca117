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
