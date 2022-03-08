#!/usr/bin/env python3

class Contact(object):
   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email

   def __str__(self):
      return f'{self.name} {self.phone} {self.email}'

class ContactList(object):
   def __init__(self):
      self.d = {}

   def add(self, c):
      self.d[c.name] = c

   def remove(self, c):
      if c in self.d:
         del self.d[c]

   def get(self, name):
      if name in self.d:
         return self.d[name]

   def __str__(self):
      lines = []
      lines.append('Contact list')
      lines.append('------------')
      for k, v in sorted(self.d.items()):
         lines.append(f'{v.name} {v.phone} {v.email}')
      return '\n'.join(lines)
