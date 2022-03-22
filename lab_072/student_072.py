#!/usr/bin/env python3

class Student(object):

   def __init__(self, sid, name, modlist=None):
      self.sid = sid
      self.name = name
      if modlist is None:
         self.modlist = []
      else:
         self.modlist = modlist

   def __str__(self):
      return f'ID: {self.sid}\nName: {self.name}\nModules: {", ".join(self.modlist)}'

   def add_module(self, module):
      self.modlist.append(module)

   def del_module(self, module):
      self.modlist.remove(module)
