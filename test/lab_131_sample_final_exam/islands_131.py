#!/usr/bin/env python3

import sys

class Graph(object):
   def __init__(self, V):
      self.adj = {}
      self.V = V
      for v in range(V):
         self.adj[v] = list()

   def addEdge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)

class DFSPaths(object):

   def __init__(self, g, s):
      self.g = g
      self.s = s
      self.visited = [False for _ in range(g.V)]
      self.parent = [False for _ in range(g.V)]
      self.dfs(s)

   def dfs(self, v):
      self.visited[v] = True
      for w in self.g.adj[v]:
         if not self.visited[w]:
            self.parent[w] = v
            self.dfs(w)

   def path(self, v):
      paths = self.visited
      return paths


def main():
   V = int(sys.stdin.readline())
   g = Graph(V)
   for line in sys.stdin:
      v, w = [int(t) for t in line.strip().split()]
      g.addEdge(v, w)

   visits = []
   for i in range(V):
      paths = DFSPaths(g, i)
      visits.append(paths.path(i))

   unique = []
   for path in visits:
      if path not in unique:
         unique.append(path)

   print(len(unique))


if __name__ == '__main__':
   main()
