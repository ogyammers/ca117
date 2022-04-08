#!/usr/bin/env python3

import sys

class Graph(object):

   def __init__(self, V):
      self.V = V
      self.adj = {}
      for v in range(V):
         self.adj[v] = list()

   def addEdge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)

   def DFS(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if visited[i] is False:
                temp = self.DFS(temp, i, visited)
        return temp

   def islands(self):
        visited = []
        islands = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] is False:
                temp = []
                islands.append(self.DFS(temp, v, visited))
        return islands

def main():
   V = int(sys.stdin.readline())
   g = Graph(V)
   for line in sys.stdin:
       v, w = [int(t) for t in line.strip().split()]
       g.addEdge(v, w)

   islands = g.islands()
   print(len(islands))


if __name__ == '__main__':
   main()
