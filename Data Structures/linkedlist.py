class Node():
  def __init__(self, value, next):
      self.value = value
      self.next = next
  
  def set_next(self, next):
    self.next = next

  def set_value(self, value):
    self.value = value

class LinkedList():
  def __init__(self):
    self.size = 0
    self.head = None

  # Adds a value to the linked list
  def add(self, val):
    node = Node(val, None)
    if (self.head == None):
      self.head = node
    else:
      curr = self.head
      while(curr.next != None):
        curr = curr.next
      curr.next = node
    self.size += 1

  # Retrieves the value at a particular position
  def get_val(self, pos):
    if pos > self.size or pos < 0:
      print("Position not in list")
    else:
      curr = self.head
      if pos > 0:
        for i in range(0,pos):
            curr = curr.next
      print(curr.value)
    return curr.value
    
  # Removes a value at a particular index
  def remove(self, pos):
    if pos >= self.size or pos < 0:
      print("Position not in list")
    else:
      self.size -= 1
      prev = self.head
      if pos == 0:
        self.head = self.head.next
      else:
        for i in range(0,pos - 1):
          prev = prev.next
        # Makes pointer of the previous node 
        # point to the next node of the node to be deleted
        curr = prev.next
        prev.next = curr.next

  # Takes a list of vals
  def add_vals(self, vals):
    for val in vals:
      self.add(val)
  
  # Returns the linked list as a regular list
  def get_list(self):
    returned_list = []
    curr = self.head
    while(curr != None):
      returned_list.append(curr.value)
      curr = curr.next
    return returned_list
  
  def get_head(self):
    return self.head.value

  def get_size(self):
    return self.size

  def is_empty(self):
    return self.size == 0
