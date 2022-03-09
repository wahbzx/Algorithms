# BFS and DFS on graphs

# Adjacency List for the graph to traverse
global adj
adj = { '1' : ['2','8'],
  '2': ['1','3','4'],
  '3': ['2'],
  '4' : ['2','5','6','8'],
  '5' : ['4'],
  '6' : ['4','7'],
  '7' : ['6','8'],
  '8' : ['1','4','7']
}

# Depth-First search
visited = set()
def dfs(start):
  visited.add(start)
  print(start)
  # Visit the first adj node of the current node
  for y in adj[start]:
    if y not in visited:
      # Perform dfs from the next node
      dfs(y) 
  # Backtrack to the parent node

# Breadth-First Search
def bfs(start):
  queue = []
  visited = set()
  visited.add(start)
  print(start)
  queue.append(start)
  # Keep repeating until no nodes are left to visit
  while len(queue) != 0:
    # pop(0) - pop from beginning of list
    y = queue.pop(0)
    # loop through all the adjacent nodes of the current node
    for z in adj[y]:
      if z not in visited:
        visited.add(z)
        print(z)
        queue.append(z)
