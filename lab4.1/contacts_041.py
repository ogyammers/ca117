#!/usr/bin/env python3

import sys

def lookup(name):
   if name in phonebook:
      return (f'Phone: {phonebook[name]}')
   return 'No such contact'


phonebook = {}
names = [line.strip() for line in sys.stdin]

with open(sys.argv[1], 'r') as f:
   contacts = [line.strip() for line in f]
   for line in contacts:
      [k, v] = line.split()
      phonebook[k] = v

for name in names:
   print(f'Name: {name}')
   print(lookup(name))
