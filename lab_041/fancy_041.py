#!/usr/bin/env python3

import sys

def lookup(name):
   if name in phonebook:
      return (f'Phone: {phonebook[name][0]}\nEmail: {phonebook[name][1]}')
   return 'No such contact'


with open(sys.argv[1], 'r') as f:
   contacts = [line.strip() for line in f]
   phonebook = {}
   for line in contacts:
      k = line.split()[0]
      v = line.split()[1:]
      phonebook[k] = v

names = [line.strip() for line in sys.stdin]

for name in names:
   print(f'Name: {name}\n{lookup(name)}')
