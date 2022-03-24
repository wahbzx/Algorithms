# Let 1 be Red and 0 be Black
class Node():
  def __init__(self, left, right, parent, val, height):
    self.left = left
    self.right = right
    self.parent = parent
    self.height = height
    self.val = val
  
class RBTree():
    def __init__(self, root):
      self.root = root

    def insert(self, node):
      if self.root == None:
        self.root = node
        node.colour = 0
      else:
        # perform a regular insertion for BST and then do recolouring or rotation
        pass
    
    def delete(self):
      # Implement delete
      pass

    def find(self):
      # Implement regular search
      pass

