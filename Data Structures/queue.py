class Node():
  def __init__(self, value, next):
      self.value = value
      self.next = next
  
  def set_next(self, next):
    self.next = next

  def set_value(self, value):
    self.value = value

class Queue():
  def __init__(self):
    self.head = None
    self.size = 0

  def enqueue(self, val):
    node = Node(val, None)
    if self.head == None:
      self.head = node
    else:
      curr = self.head
      while curr.next != None:
        curr = curr.next
      curr.next = node
    self.size += 1

  def dequeue(self):
    if self.head == None:
      print("Queue is empty!")
      return None
    else:
      node = self.head
      self.head = self.head.next
      self.size -= 1
      return node.value
  
  def enqueue_all(self, vals):
    for val in vals:
      self.enqueue(val)
  
  def dequeue_all(self):
    queue = []
    while self.size > 0:
      queue.append(self.dequeue())
    return queue

  def is_empty(self):
    return self.size == 0
