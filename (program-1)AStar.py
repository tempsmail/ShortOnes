import numpy as np
import pandas as pd

def Astar(start_node,stop_node):
  open_set=set(start_node)
  closed_set=set()
  g={}
  parents={}
  parents[start_node]=start_node
  g[start_node]=0
  while len(open_set) > 0:
    n=None
    for w in open_set:
      if n==None or g[w]+heuristic(w) < g[n]+heuristic(n):
        n=w
    if n==stop_node or Graph_node(n)==None:
      pass
    else:
      for (m,weight) in get_neighbors(n):
        if m not in open_set and m not in closed_set:
          open_set.add(m)
          g[m]=g[n]+weight
          parents[m]=n
        else:
          if g[m]>g[n]+weight:
            g[m]=g[n]+weight
            parents[m]=n
            if m in closed_set:
              closed_set.remove(m)
              open_set.add(m)
    if n==None:
      print("Path not found")
      return None
    if n==stop_node:
      path=[]
      while parents[n]!=n:
        path.append(n)
        n=parents[n]
      path.append(start_node)
      path.reverse()
      print('Path found : {} '.format(path))
      return path
    open_set.remove(n)
    closed_set.add(n)
 print('Path not found')
 return None
def get_neighbor(val):
  if val in graph_node:
    return graph_node[val]
  else:
    return None
def heuristics(val):
  H={
    'A':11,
    'B':6,
    'C':5,
    'D':3
  }
  return H[val]
graph_node={
  'A':{('B',6)},
  'B': [('A', 6), ('C', 3), ('D', 2)],
  'C': [('B', 3), ('D', 1)],
  'D': [('B', 2), ('C', 1)]
}
Astar('A','D')
