class Node():
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val

def insert(node, val):
  if node.val < val:
    if node.right == None:
      node.right = Node(val)
    else:
      insert(node.right, val)
  elif node.val > val:
    if node.left == None:
      node.left = Node(val)
    else:
      insert(node.left, val)
  # else:
    #print(val,"already exists in tree")

def getBiggest(tree):
  if tree.right == None:
    return tree.val
  else:
    return getBiggest(tree.right)

def getSmallest(tree):
  if tree.left == None:
    return tree.val
  else:
    return getSmallest(tree.left)

def exists(tree, val):
  if tree.val != val and tree.right == None and tree.left ==None:
    return False
  elif tree.val == val:
    return True
  else:
    if tree.val < val:
      return exists(tree.right, val)
    else:
      return  exists(tree.left, val)

# * unpacks contents list and putting it in [] 
# packs into a list again hence flattening the list
def get_list(tree):
  if tree.left == None and tree.right == None:
    return [tree.val]
  elif tree.left != None and tree.right == None:
    l = [*get_list(tree.left), tree.val]
    return l
  elif tree.left == None and tree.right != None:
    l = [] 
    l = [tree.val, *get_list(tree.right)]
    return l
  elif tree.left != None and tree.right != None:
    l = [*get_list(tree.left), tree.val, *get_list(tree.right)]
    return l

def from_list(list):
  node = Node(list[0])
  for i in list[1:]:
    insert(node,i)
  return node
