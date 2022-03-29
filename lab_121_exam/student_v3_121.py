grades = {'H1': 100, 'H2': 88, 'H3': 77, 'H4': 66, 'H5': 56,
          'H6': 46, 'H7': 37, 'H8': 0, 'O1': 56, 'O2': 46,
          'O3': 37, 'O4': 28, 'O5': 20, 'O6': 12, 'O7': 0, 'O8': 0}

def grade2points(grade):
    return grades[grade]


class Student(object):
   def __init__(self, name, cao):
      self.name = name
      self.cao = cao
      self.d = {}

   def __str__(self):
      return f'Name: {self.name}\nCAO: {self.cao}\nPoints: {self.total_grades()}'

   def add_grade(self, subject, grade):
      self.d[subject] = grade2points(grade)

   def get_grade(self, subject):
      if subject in self.d:
         return self.d[subject]
      return 'N/A'

   def total_grades(self):
      output = [g for g in sorted(self.d.values())]
      if len(output) < 4:
        return sum(output)
      else:
        return output[-3] + output[-2] + output[-1]
