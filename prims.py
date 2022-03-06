from math import inf
import heapq
from os import stat

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

# Classical Prim's - better when graph is dense
def prims(start):
  # Initialise tree with starting node
  weight = {}
  tree = set()
  fringe = set()
  tree.add(start)
  print("Adding node: ", start)
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

def heappop(pq):
  # Heapq orders the PQ by the key rather than value - so switch them around
  new_pq = [(b,a) for (a,b) in list(pq.items())]
  # heapify orders new_pq in order to make it a priority queue
  heapq.heapify(new_pq)
  # Returns the Node with the smallest val
  (val,key) = heapq.heappop(new_pq)
  return (key,val)

# Prim's using a priority queue - Better when graph is sparse
def prims_pq(start):
  # The priority queue will contain key val pairs
  # Key - fringe node
  # Val - cost to travel to it from the tree
  pq = {}
  tree = set()
  # Initialise the PQ where all the costs are infinity
  for x in adj:
    pq[x] = inf
  pq = [(b,a) for (a,b) in list(pq.items())] 
  heapq.heapify(pq)
  pq = dict([(b,a) for (a,b) in pq])
  # cost to travel from start to start is 0
  pq[start] = 0
  while len(pq) > 0:
    # Returns the node with the smallest cost to travel to from tree
    (f,v) = heappop(pq)
    # Remove this node from the PQ and adds it to the tree
    pq.pop(f)
    tree.add(f)
    print("Adding node: ",f)
    # Checks adjacent fringe nodes of the newly added node
    # If they are not in already in the tree and the cost is cheaper from the newly added node
    # Then before, then it will update the cost to travel to the fringe node
    for y in adj[f]:
      if y not in tree and weight_matrix[f][y] < pq[y]:
        pq[y] = weight_matrix[f][y]
  print("Done")
  print(tree)


# Example MST from 0: 
# prims(0)
# prims_pq(0)