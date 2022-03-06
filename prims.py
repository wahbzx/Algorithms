from math import inf
import heapq

# Example weighted graph
adj = { 0: [1,2,3],
        1: [0,2],
        2: [0,1,3],
        3: [0,2]
}
weight_matrix = [[inf,3,5,4],
                 [3,inf,4,inf],
                 [5,4,inf,2],
                 [4,inf,2,inf]]

def prims(start):
  # Initialise tree with starting node
  weight = {}
  tree = set()
  fringe = set()
  tree.add(start)
  # Add all the connected nodes to the tree to the fringe
  for i in adj[start]:
    fringe.add(i)
    weight[i] = weight_matrix[start][i]
  # End of initialisation
  while len(fringe) > 0:
    # Find minimum weigth in fringe
    min_key = min(weight, key=weight.get)
    tree.add(min_key)
    print("Adding Node: ",min_key)
    # Remove the node added to the tree from the fringe
    fringe.remove(min_key)
    weight[min_key] = inf
    # Adds all the adj nodes of the added node to the fringe
    for y in adj[min_key]:
      if y not in tree:
        if y in fringe:
          # If the adj node was already in the fringe but the arc from the new node
          # To the adj node is shorter it will replace that arc to be the shortest path from the tree
          # to the fringe node
          if weight_matrix[min_key][y] < weight[y]:
            weight[y] = weight_matrix[min_key][y]
          # Otherwise it will add the node to the fringe
          else:
            fringe.add(y)
            weight[y] = weight_matrix[min_key][y]
  print("Done")
  print(tree)

# Prim's using a priority queue - heapq is the priority queue implementation in python
def prims_pq(start):
  pass

# Example MST from 0: prims(0)
