class Node():
  def __init__(self, value, next):
      self.value = value
      self.next = next
  
  def set_next(self, next):
    self.next = next

  def set_value(self, value):
    self.value = value

class Stack():
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, val):
    node = Node(val, None)
    if self.head == None:
      self.head = node
    else:
      node.next = self.head
      self.head = node
    self.size += 1

  def pop(self):
    if self.size > 0:
      node = self.head
      self.head = self.head.next
      self.size -= 1
      return node.value
    else:
      print("Stack is empty!")
      return None

  def push_all(self, vals):
    for val in vals:
      self.push(val)

  def pop_all(self):
    stack = []
    for i in range(0, self.size):
      stack.append(self.pop())
    return stack

  def peek(self):
    return self.head.value

  def peek_all(self):
    stack = []
    curr = self.head
    while curr != None:
      stack.append(curr.value)
      curr = curr.next
    return stack

  def is_empty(self):
    return self.size == 0
