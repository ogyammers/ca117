#!/usr/bin/env python3

import sys

def hotel(line):
   rooms, occupied = line[0], line[1:]   
   available = [i for i in range(1, int(rooms)) if str(i) not in occupied]
   
   if available == []:
      return 'no room'
   
   return sorted(available)[0]

def main():
   print(hotel(sys.stdin.readline()))

if __name__ == '__main__':
   main()

