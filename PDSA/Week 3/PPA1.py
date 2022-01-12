class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
class doubly_linked_list:
  def __init__(self):
    self.head = None
    self.last = None
  def insert_end(self, data):
    newNode = Node(data)
    newNode.prev = self.last
    if(self.head == None):
        self.head = newNode
        self.last = newNode
    else:
        self.last.next = newNode
        self.last = newNode
  def delete_end(self):
    if(self.head != None):
        if(self.head == self.last):
            self.head = None
            self.last = None
        else:
            self.last = self.last.prev
            self.last.next=None
        