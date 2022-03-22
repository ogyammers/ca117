#!/usr/bin/env python3

class Student(object):

   def set_attributes(self, sid, name, modlist):
      self.sid = sid
      self.name = name
      self.modlist = modlist

   def print_attributes(self):
      print(f'ID: {self.sid}\nName: {self.name}\nModules: {", ".join(self.modlist)}')

   def add_module(self, module):
      self.module = module
      self.modlist.append(self.module)

   def del_module(self, module):
      self.module = module
      self.modlist.remove(self.module)
