#!/usr/bin/env python3

class Queue(object):

   def __init__(self):
      self.list = []

   def enqueue(self, q):
      self.list.insert(0, q)

   def dequeue(self):
      return self.list.pop()

   def first(self):
      return self.list[-1]

   def is_empty(self):
      return len(self.list) == 0

   def __len__(self):
      return len(self.list)
